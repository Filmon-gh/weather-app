# Import the required modules
import requests  # Import the requests module for making HTTP requests
import json  # Import the json module for working with JSON data
import time
from datetime import datetime  # Import the datetime module for working with dates and times


API_KEY = "6112a97c554eb760c42d9012cfc32ad6"
API_URL = "https://api.openweathermap.org/data/2.5/weather"


# Function to retrieve weather data from the OpenWeatherMap API for a given city name
def get_weather_data(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY
    }
    response = requests.get(API_URL, params=params)
    return response.json()


# Accessing specific weather data
def get_specific_weather_data(weather_data):
    temperature_kelvin = weather_data['main']['temp']
    temperature_celsius = temperature_kelvin - 273.15
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']
    wind_speed = weather_data['wind']['speed']

    weather_info = {
        'Temperature': f"{temperature_celsius:.2f} °C",
        'Humidity': f"{humidity}%",
        'Description': description,
        'Wind Speed': f"{wind_speed} m/s"
    }

    return weather_info


# Function to print weather data
def print_weather_data(weather_info, city_name):
    print(f"City: {city_name}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d')}")

    for key, value in weather_info.items():
        print(f"{key}: {value}")

    description = weather_info['Description'].lower()

    if 'rain' in description:
        print("\nRemember to bring an umbrella!\n")
    elif 'cloud' in description:
        print("\nIt's a cloudy day.\n")
    elif float(weather_info['Temperature'].split()[0]) > 25:
        print("\nIt's hot outside. Stay hydrated!\n")
    elif float(weather_info['Temperature'].split()[0]) < 5:
        print("\nIt's cold outside. Bundle up!\n")
    else:
        print("\nEnjoy the weather!\n")


def display_weather_data(weather_data, city_name):
    if 'cod' in weather_data and weather_data['cod'] != 200:
        # If the 'cod' key is present in weather_data and its value is not 200
        # (indicating an error response from the API)
        print(f"Error: {weather_data['message']}")
    else:
        try:
            weather_info = get_specific_weather_data(weather_data)
            current_date = datetime.now().strftime('%Y-%m-%d')
            print_weather_data(weather_info, city_name)
        except KeyError:
            print("Invalid weather data. Unable to display.")


# Continuously prompts the user to enter a new city name and retrieves and displays the weather data for the entered city.
# The loop continues until the user enters 'q' to quit.
def retrieve_weather_data():
    while True:
        option = input("Enter a new city (or 'q' to quit): ")
        if option.lower() == 'q':
            break
        if not option.strip():
            print("Please enter a valid city")
            continue
        city_name = option
        weather_data = get_weather_data(city_name)
        display_weather_data(weather_data, city_name)


if __name__ == '__main__':
    retrieve_weather_data()
