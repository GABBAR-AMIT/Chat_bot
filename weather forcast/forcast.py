import requests
import json
import datetime


def get_weather_forecast(location):
    """
    Retrieves the weather forecast for the next 7 days from the current date.

    Args:
        location (str): The location for which the forecast is requested.

    Returns:
        dict: The weather forecast data for the next 7 days.
    """
    # Insert your API key here
    api_key = "fe6dff6186074f0fb0c0a5e73bbc3107"

    # Construct the API URL with the location and API key, https://api.weatherbit.io
    url = f"https://api.weatherbit.io/v2.0/forecast/daily?city={location}&key={api_key}&days=7"

    try:
        # Send the request to the API
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = json.loads(response.text)

            # Extract the forecast data for the next 7 days
            forecast = data["data"]

            return forecast
        else:
            print("Failed to retrieve weather forecast. Please try again.")
            print(response.text)  # Print the response text for debugging
    except requests.exceptions.RequestException:
        print("An error occurred while making the API request. Please try again.")

    return None


def print_weather_forecast(forecast):
    """
    Prints the weather forecast in a tabular manner.

    Args:
        forecast (dict): The weather forecast data for the next 7 days.
    """
    if not forecast:
        print("No forecast data available.")
        return

    print("Weather Forecast:")
    print("-" * 50)
    print("| Date                | Temperature (C) | Weather Condition     |")
    print("-" * 50)

    for day in forecast:
        date = day["valid_date"]
        temperature = day["temp"]
        condition = day["weather"]["description"]

        print(f"| {date} | {temperature:^15} | {condition:^22} |")

    print("-" * 50)


def save_weather_forecast(location, forecast):
    """
    Saves the weather forecast in a file with the location in the filename.

    Args:
        location (str): The location for which the forecast is requested.
        forecast (dict): The weather forecast data for the next 7 days.
    """
    filename = f"forecast_{location.replace(' ', '_')}.txt"

    with open(filename, "w") as file:
        file.write("Weather Forecast:\n")
        file.write("-" * 50 + "\n")
        file.write("| Date                | Temperature (C) | Weather Condition     |\n")
        file.write("-" * 50 + "\n")

        for day in forecast:
            date = day["valid_date"]
            temperature = day["temp"]
            condition = day["weather"]["description"]

            file.write(f"| {date} | {temperature:^15} | {condition:^22} |\n")

        file.write("-" * 50 + "\n")

    print(f"Forecast saved to {filename}")


# Main program
if __name__ == "__main__":
    # Ask the user for the location
    location = input("Enter a location: ")

    # Get the weather forecast
    forecast = get_weather_forecast(location)

    if forecast:
        # Print the weather forecast
        print_weather_forecast(forecast)

        # Save the weather forecast to a file
        save_weather_forecast(location, forecast)
