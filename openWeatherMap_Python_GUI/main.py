import requests
from tkinter import *
import math

city = "city here"
api_key = "key here"

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/3.0/weather?q={city}&appid={api_key}"

    response = requests.get(url).json()

    temperature = response['main']['temp']
    temperature = math.floor((temperature * 1.8) + 32)  # Convert to °F

    feels_like = response['main']['feels_like']
    feels_like = math.floor((feels_like * 1.8) + 32)  # Convert to °F

    humidity = response['main']['humidity']
    
    return {
        'temp': temp,
        'feels_like': feels_like,
        'humidity': humidity
    }

weather = get_weather(api_key, city_name)

root = Tk()
root.geometry("300x300")
root.title(f'{city[:-3]} Weather')

def display_city_name(city):
    city_label = Label(root, text=f"{city[:-3]}")
    city_label.config(font=("Consolas", 28))
    city_label.pack(side='top')

def display_stats(weather):
    temp = Label(root, text=f"Temperature: {weather['temp']} F")
    feels_like = Label(root, text=f"Feels Like: {weather['feels_like']} F")
    humidity = Label(root, text=f"Humidity: {weather['humidity']} %")

    temp.config(font=("Consolas", 22))
    feels_like.config(font=("Consolas", 16))
    humidity.config(font=("Consolas", 16))

    temp.pack(side='top')
    feels_like.pack(side='top')
    humidity.pack(side='top')


display_city_name(city)
display_stats(weather)

mainloop()
