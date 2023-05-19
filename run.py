# Import the required modules
import requests  
import json  
from datetime import datetime  


class WeatherApp:
    # WeatherApp class encapsulating the functionality of the weather app

    API_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key):
        # Initializes the WeatherApp object with the provided API key
        self.api_key = api_key

    def get_weather_data(self, city_name):
        """
        Retrieves weather data from the OpenWeatherMap API
        for the given city name
        """
        params = {
            'q': city_name,
            'appid': self.api_key
        }
        response = requests.get(self.API_URL, params=params)
        return response.json()

    def get_specific_weather_data(self, weather_data):
        # Extracts specific weather data from the weather data response
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

    def print_weather_data(self, weather_info, city_name):
        # Prints the weather data for the given city
        current_date = datetime.now().strftime('%Y-%m-%d')
        print(f"\nCity: {city_name}")
        print(f"Date: {datetime.now().strftime('%Y-%m-%d')}\n")

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

        print("-" * 40)  # Add a dashed line separator    

    def print_error_message(self, error_message):
        # Prints error messages based on the error response from the API
        if error_message == 'city not found':
            print("Error: City not found. Please enter a valid city name.")
        else:
            print(f"Error: {error_message}")

    def display_weather_data(self, weather_data, city_name):
        # Displays the weather data for the given city
        if 'cod' in weather_data and weather_data['cod'] != 200:
            self.print_error_message(weather_data['message'])
        else:
            try:
                weather_info = self.get_specific_weather_data(weather_data)
                self.print_weather_data(weather_info, city_name)
            except KeyError:
                print("Invalid weather data. Unable to display.")

    def retrieve_weather_data(self):
        welcome_message = "Welcome to the Weather App!"  # Define the welcome message
        margin = (50 - len(welcome_message)) // 2  # Calculate the margin for center alignment
        print(" " * margin + welcome_message)  # Print the centered message
        print()  # Add an empty print statement for the space
        print("This app provides current weather information for a given city.")
        print("Enter the name of a city to get its current weather information.")
        print("Enter 'q' to quit the application.")
        print()  # Add an empty print statement for the space
        print("-" * 50)  # Add a dashed line separator
        
        # Prompts the user to enter a new city or 'q' to quit
        while True:
            option = input("Enter a new city (or 'q' to quit):\n")
            if option.lower() == 'q':
                print("Quitting the application...")
                print("-" * 50)  # Add a dashed line separator
                return  # Exit the method and return to the main part of the application   
            option = option.strip()  # Remove leading and trailing space
            if not option.strip():
                print("Please enter a valid city")
                continue
            city_name = option
            weather_data = self.get_weather_data(city_name)
            self.display_weather_data(weather_data, city_name)


if __name__ == '__main__':
    # Main part of the Python application
    api_key = "6112a97c554eb760c42d9012cfc32ad6"
    app = WeatherApp(api_key)
    app.retrieve_weather_data()
