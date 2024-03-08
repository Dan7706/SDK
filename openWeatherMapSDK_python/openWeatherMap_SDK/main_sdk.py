from api import OpenWeatherMapAPI
from datetime import datetime, timedelta

class OpenWeatherMapSDK:
    def __init__(self, apikey, mode='on-demand'):
        self.api = OpenWeatherMapAPI(apikey)
        self.mode = mode
        self.weather_cache = {}
    
    def __del__(self):
        print("OpenWeatherMapAPI instance deleted!")

    def get_city_weather(self, city):
        """This function checks the city weather information in cache"""
        if city not in self.weather_cache or self._is_cache_expired(city):
            if self.mode == 'polling':
                self._update_weather_cache()
            else:
                self._update_weather_cache(city)
            return self.weather_cache.get(city)

    def _update_weather_cache(self, city=None):
        """This function updates cache for getting the latest info from API 
        and give user with low latency"""
        if city:
            weather_data = self.api.get_weather(city)
            self.weather_cache[city] = weather_data
        else:
            for mycity in list(self.weather_cache.keys()):
                weather_data = self.api.get_weather(mycity)
                self.weather_cache[mycity] = weather_data

    def _is_cache_expired(self, city):
        """This function checks the cache expired ot not, and return a bollean for 
        updating cache every 10 minutes"""
        if city in self.weather_cache:
            last_updated = datetime.fromtimestamp(self.weather_cache[city]['dt'])
            return datetime.now() - last_updated > timedelta(minutes=10)
        return True

    def delete_city_cache(self, city):
        """This function deletes the current city from the cache"""
        if city in self.weather_cache:
            del self.weather_cache[city]
