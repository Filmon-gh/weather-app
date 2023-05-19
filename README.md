
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

## Weather Data Retrieval: 

![App Screenshot]()

- The app retrieves weather data from the OpenWeatherMap API based on the user-entered city name.


## Specific Weather Data:

![App Screenshot]()
- The app extracts specific weather information from the API response, including temperature, humidity, description, and wind speed. 



## Print Weather Data:

  The app prints the retrieved weather data, including the city name, date, temperature, humidity, description, and wind speed 

![App Screenshot]()

## Additional Weather Information:

 <img src=""  height="250"/> 

The app provides additional information based on the weather conditions. It prompts reminders for bringing an umbrella in case of rain, mentions if it's a cloudy day, advises staying hydrated if it's hot outside, suggests bundling up in cold weather, and encourages enjoying the weather otherwise.
 
## Error Handling:
The app handles errors gracefully, such as when a city is not found or when there are issues with the API response. It displays appropriate error messages to the user.

![App Screenshot]()

## User Interaction: 
 <img src="https://raw.githubusercontent.com/Filmon-gh/Delicous-Restuarant/49a745e4a1e8cf8c61fd871f8e18a06d78f0764a/screenshots/screenshotimge/7.%20menu.JPG"  height="600" width="500" /> 

- The app allows users to enter new city names to retrieve and display weather data. It provides the option to quit the application by entering 'q'. 
 

## Features to be added in the future
 - Forecast Information: Extend the app to retrieve and display weather forecasts for multiple days instead of just the current weather. Users can get a better understanding of the weather conditions over a specific period.
 - Temperature Conversion: The app could provide an option for users to choose between Celsius and Fahrenheit temperature units for displaying the weather information.
 - Graphical Visualization: Incorporate graphical visualization of weather data using charts or graphs. This feature provides users with a visual representation of temperature variations, humidity levels, or wind speeds over a specific period, improving data interpretation.
 - Multiple Cities: Enhance the app to support retrieving and displaying weather data for multiple cities at once. Users can enter a list of cities separated by commas to get weather information for each city in a consolidated output.

## Technology Used: 

 - GitHub: The project hosted on GitHub, a web-based hosting service for version control using Git. 

 
## Testing 

The Weather App has been tested using both manual and automated testing approaches to ensure its functionality and accuracy in retrieving and displaying weather data.  

 - Input Validation: The application has been tested to validate user input for city names. Various scenarios, including empty input, invalid city names, and valid city names, have been tested to ensure proper error handling and response.

 - API Integration: The Weather App has been tested by making requests to the OpenWeatherMap API with different city names to verify the successful retrieval of weather data. The responses have been validated for correctness and adherence to the expected format. 

 - Edge Cases: The application has been tested with extreme weather conditions, such as very high and very low temperatures, to ensure accurate temperature conversion and appropriate messages based on the weather conditions. 


## Bugs



 <img src="" height="250"/> 




## Validator Testing



## Deployment 


## Credits 
  