
# Weather Forecast Script 🌡️ 
This Python script retrieves the weather forecast for the next 7 days using the Weatherbit API based on the user's input location. The script can print the forecast in a tabular format or save it to a file.


## Prerequisites
- Python 3.x
- Requests library (pip install requests)


## Usage
- Obtain an API key from Weatherbit by signing up for a free account.
- Insert your API key into the api_key variable in the script.
- Run the script using the command python weather_forecast.py.
- Enter the location for which you want to retrieve the weather forecast when prompted.
- The script will fetch the forecast, display it on the console, and save it to a file named forecast_location.txt.


## Example Output
Enter a location: New York
Weather Forecast:
--------------------------------------------------
| Date                | Temperature (C) | Weather Condition     |
--------------------------------------------------
| 2023-06-14          |      20.2       |        Cloudy         |
| 2023-06-15          |      22.5       |     Partially cloudy  |
| 2023-06-16          |      21.8       |        Rain           |
| 2023-06-17          |      19.6       |     Partially cloudy  |
| 2023-06-18          |      23.7       |        Clear          |
| 2023-06-19          |      25.1       |     Partially cloudy  |
| 2023-06-20          |      24.8       |     Partially cloudy  |
--------------------------------------------------
Forecast saved to forecast_New_York.txt

## Limitations
- The script assumes a successful API response with a status code of 200. It may not handle all possible error scenarios.
- The API key provided in the script is for demonstration purposes only. It is recommended to use your own API key.

## 🚀 About Me
I'm a Python developer...


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/amit-kumar-sahu7941//)

## Authors

- [@GABBAR-AMIT](https://github.com/GABBAR-AMIT)
