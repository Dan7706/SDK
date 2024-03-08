# General Information
This SDK is based on OpenWeatherMap API and gives an opportunity to get weather information
without any complexity.

# Installing 
    pip install openWeatherMap_SDK

# Usage
    create an instance on class OpenWeatherMapSDK:
    weather = OpenWeatherMapSDK(apikey="Your_API_key_here")

# Functionals
    Insert a city where you want to get weather information.
    city_weather = weather.get_city_weather():
    city = input("Enter city for weather broadcast: ")



# Publishing this package to PYPI 

To publish your pakaches to PYPI you can use twine tool 
    twine upload dist/*

You will be prompted for your PYPI creditentials. Once uploaded anyone can install your package and use.
    pip install openWeatherMap_SDK

#Useful links
-[Python packaging user guide](https://packaging.python.org)
-[setuptools documentation](https://setuptools.readthedocs.io)
