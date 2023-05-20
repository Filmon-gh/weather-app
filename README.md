
#  Weather-App     
The Weather App is a Python application that retrieves and displays weather data for user-entered city names. It utilizes the OpenWeatherMap API to fetch weather information such as temperature, humidity, description, and wind speed for the specified city.
 

<img src=""  width="900" /> 

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

<img src=""  height="" width="" /> 

-  The app presents a welcoming message and app instructions upon startup, making it easy for users to understand how to interact with the application.


## City-specific Weather Information:

<img src=""  height="" width="" /> 

- The app retrieves weather data from the OpenWeatherMap API based on the user-entered city name.
- Enter the name of a city to get its current weather data, including temperature, humidity, description, and wind speed.


## Print Weather Data:

  The app prints the retrieved weather data, including the city name, date, temperature, humidity, description, and wind speed.

<img src=""  height="" width="" /> 

## Weather Conditions: 
 <img src=""  height=""/> 

The app provides additional information based on the weather conditions. It prompts reminders for bringing an umbrella in case of rain, mentions if it's a cloudy day, advises staying hydrated if it's hot outside, suggests bundling up in cold weather, and encourages enjoying the weather otherwise.

## User Interaction: 
 <img src=""  height="" width="5" /> 

- The app allows users to enter new city names to retrieve and display weather data. It provides the option to quit the application by entering 'q'. 
 
## Error Handling:
The app handles errors smoothly, such as when a city is not found or when there are issues with the API response. It displays appropriate error messages to the user.

<img src=""  height="" width="" /> 


 

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
 # Remove leading and trailing whitespace characters from the user's input
option = option.strip()

# Check if the stripped option is empty or contains only whitespace
if not option.strip():
    print("Please enter a valid city")
    continue


 <img src="" height=""/> 




## Validator Testing



## Deployment 


## Credits 
  