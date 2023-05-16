# Import the required modules
import requests  # Import the requests module for making HTTP requests
import json  # Import the json module for working with JSON data
from tkinter import *  # Import the tkinter module for GUI
from datetime import datetime  # Import the datetime module for working with dates and times




API_key="6112a97c554eb760c42d9012cfc32ad6"
city_name=input("Enter your city: ")
# Construct the URL with API key and location
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
# Make the API request
response = requests.get(url)
weather_data=response.json()


# Accessing specific weather data
temperature_kelvin = weather_data['main']['temp']
temperature_celsius = temperature_kelvin - 273.15
humidity = weather_data['main']['humidity']
description = weather_data['weather'][0]['description']
wind_speed = weather_data['wind']['speed']

# Printing weather data using f-strings
print(f"City: {city_name}")
print(f"Temperature: {temperature_celsius:.2f} °C")
print(f"Humidity: {humidity}%")
print(f"Description: {description}")
print(f"Wind Speed: {wind_speed} m/s")


