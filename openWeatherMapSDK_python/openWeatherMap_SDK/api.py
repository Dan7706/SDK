import requests
from datetime import datetime, timedelta

class OpenWeatherMapAPI:
    __slots__ = ("api_key", "lang", "base_url")

    def __init__(self, apikey: str= "", lang: str='en'):
        self.api_key = apikey
        self.lang = lang
        self.base_url = "https://api.openweathermap.org/data/3.0/weather?"


    class APIError(Exception):
        print("Your API key is not valid or out of date! Please check it and try again!")
        

    def get_weather(self):
        city = input("Enter city for weather broadcast: ")
        params = {
            'q': city,
            'lang': self.lang,
            'appid': self.api_key,
        }
        if self.api_key != "":
            params["appid"] = self.api_key
            try:
                response = requests.get(self.base_url, params=params)
            except requests.exceptions.RequestException as err:
                raise self.APIError(f"Request Exception: {err}")

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()


