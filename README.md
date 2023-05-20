
#  Weather-App     
The Weather App is a Python application that retrieves and displays weather data for user-entered city names. It utilizes the OpenWeatherMap API to fetch weather information such as temperature, humidity, description, and wind speed for the specified city.
 

<img src="https://raw.githubusercontent.com/Filmon-gh/weather-app-python/0077498c80be08bcf2fca9ca9591eb1c47382340/screen-shots/display.png"  width="" /> 

## User stories
 The following user stories have been identified: 

- As a user, I want to be able to enter the name of a city and retrieve the current weather information for that city.

- As a user, I want the weather information to include the temperature in Celsius, humidity percentage, weather description, and wind speed. 

- As a user, I want the app to provide additional messages based on the weather conditions, such as reminders to bring an umbrella if it's raining or alerts about extreme temperatures.

- As a user, I want the app to handle errors gracefully and provide user-friendly error messages. 
- As a user, I want the app to display the date of the weather information, so I know how recent it is.

- As a user, I want the app to be fast and responsive, so I can quickly retrieve weather information for different cities.



# Features

## Dynamic User Interface:

   <img src="https://raw.githubusercontent.com/Filmon-gh/weather-app-python/41cf75733da5cc7f14c697c83f56a2144b3b6d1d/screen-shots/welcome.png"/> 

-  The app presents a welcoming message and app instructions upon startup, making it easy for users to understand how to interact with the application.


## City-specific Weather Information:
- The app retrieves weather data from the OpenWeatherMap API based on the user-entered city name.
- Enter the name of a city to get its current weather data, including temperature, humidity, description, and wind speed.

<img src="https://raw.githubusercontent.com/Filmon-gh/weather-app-python/b84835eecae4ed02ea379eb96bf5cfb97a4e6c31/screen-shots/body.png" /> 

## User Interaction: 
- The app allows users to enter new city names to retrieve and display weather data. It provides the option to quit the application by entering 'q'.

## Weather Conditions: 
 
The app provides additional information based on the weather conditions. It prompts reminders for bringing an umbrella in case of rain, mentions if it's a cloudy day, advises staying hydrated if it's hot outside, suggests bundling up in cold weather, and encourages enjoying the weather otherwise.
  
### Error Handling:
The app handles errors smoothly, such as when a city is not found or when there are issues with the API response. It displays appropriate error messages to the user.

### Invalid City Input

When a user enters a wrong city name or keyword, the Weather App detects this and displays an error message to inform the user about the invalid input. The error message clearly states that the entered city is not found and prompts the user to enter a valid city name.

Example Error Message:

<img src="https://raw.githubusercontent.com/Filmon-gh/weather-app-python/35160bab21544593a8e2c28b00d6403c95efcd89/screen-shots/error.png" /> 

### Empty Input

To prevent the app from processing empty input (blank spaces or pressing enter without providing a city name), special error handling has been implemented. When the user enters empty input, the app detects it and displays an appropriate error message, prompting the user to enter a valid city name.

Example Error Message:

<img src="https://raw.githubusercontent.com/Filmon-gh/weather-app-python/bbdefc8ce72e669ddff1c2a187da404a7a39386f/screen-shots/error2.png"/>

## Features to be added in the future
 - Forecast Information: Extend the app to retrieve and display weather forecasts for multiple days instead of just the current weather. Users can get a better understanding of the weather conditions over a specific period.
 - Temperature Conversion: The app could provide an option for users to choose between Celsius and Fahrenheit temperature units for displaying the weather information.
 - Graphical Visualization: Incorporate graphical visualization of weather data using charts or graphs. This feature provides users with a visual representation of temperature variations, humidity levels, or wind speeds over a specific period, improving data interpretation.
 

## Technology Used: 

 This project utilizes the following technologies:

 - Python: The Weather App is written in Python, leveraging its simplicity and versatility.

 - requests: The requests library is used to make HTTP requests to the OpenWeatherMap API and retrieve weather data.

 - JSON: JSON (JavaScript Object Notation) is used to handle weather data responses from the OpenWeatherMap API. The json module is imported to work with JSON data.

 - datetime: The datetime module is used to handle date and time operations, such as getting the current date.

 - CodeAnywhere: CodeAnywhere, a cloud-based integrated development environment (IDE), was used for coding and development of the Weather App.

 - GitHub: GitHub, a web-based version control repository hosting service, was utilized for storing and managing the code repository. 

 - Heroku: The Weather App is deployed to Heroku, which provides an environment to host the app and make it accessible online.
 
## Testing 

The Weather App has been tested using both manual and automated testing approaches to ensure its functionality and accuracy in retrieving and displaying weather data.  

 - Input Validation: The application has been tested to validate user input for city names. 
 Various scenarios, including empty input, invalid city names, and valid city names, have been tested to ensure proper error handling and response.

 - API Integration: The Weather App has been tested by making requests to the OpenWeatherMap API with different city names to verify the successful retrieval of weather data. The responses have been validated for correctness and adherence to the expected format. 

 - Edge Cases: The application has been tested with extreme weather conditions, such as very high and very low temperatures, to ensure accurate temperature conversion and appropriate messages based on the weather conditions. 


## Bugs
The app was experiencing a bug related to user input handling, specifically when users entered blank spaces or pressed enter without providing a city name.The app did not handle this scenario correctly, leading to unexpected behavior and potential errors.

To address the bug where the app did not handle blank spaces or empty input correctly, the following changes were made:

 - Added the option.strip() method to remove leading and trailing whitespace characters from the user's input.
 - Modified the condition to check if the stripped option is empty or contains only whitespace.
 - If the condition evaluates to True, an appropriate error message is displayed, prompting the user to enter a valid city name.

The fixed code snippet is as follows:
  - Remove leading and trailing whitespace characters from the user's input
option = option.strip()

 - Check if the stripped option is empty or contains only whitespace
if not option.strip():
    print("Please enter a valid city")
    continue


## Validator Testing

Tool: PEP8 

Summary: No Errors Found

## Deployment 

This project is deployed to Heroku, a cloud platform that allows for easy deployment and hosting of web applications.

 - Clone the GitHub repository: Clone the Weather App repository from GitHub and ensure the necessary permissions to access the repository.
  - Create a Heroku app:
  - Navigate to the "Settings" tab in the Heroku app settings.
           - Locate the "Buildpacks" section.
            - Add the necessary buildpacks by including the Python buildpack and Node.js buildpack.

  - Link the Heroku app to the repository.

 - Deploy to Heroku:

## Credits 

I learned about the implementation and understanding of weather app codes, as well as retrieving data from the weather API, from the following sources:

 - AskPython: "GUI Weather App in Python" (Website) Link: https://www.askpython.com/python/examples/gui-weather-app-in-python
The code and concepts presented in this AskPython tutorial provided valuable insights into the process of retrieving data from a weather API.

 - YouTube: "Creating a Weather App in Python" (Video) Link: https://www.youtube.com/watch?v=7JoMTQgdxg0
 
 The YouTube tutorial on creating a weather app in Python offered additional guidance and practical examples for implementing weather-related functionality. It assisted in understanding key concepts, such as making HTTP requests to an API and extracting specific weather data.

 - In addition, this weather app utilizes the OpenWeatherMap API (https://openweathermap.org) to retrieve current weather data for a given city. The OpenWeatherMap API provides comprehensive weather information, including temperature, humidity, description, and wind speed, which are displayed within the app's user interface.

By combining the knowledge gained from these resources and leveraging the OpenWeatherMap API, I was able to develop this weather app and adapt it to suit my specific requirements. 