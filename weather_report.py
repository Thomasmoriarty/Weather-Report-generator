import requests
#API key: 5152731c5f39beda8451a898b85d55dc
def get_weather(city_name, api_key):
    # Define the API endpoint URL
    endpoint = "http://api.openweathermap.org/data/2.5/weather"

    # Pass the city name and API key as parameters to the endpoint URL
    parameters = {
        "q": city_name,
        "appid": api_key
    }

    # Make the API request using the requests module
    response = requests.get(endpoint, params=parameters)

    # Check if the API request was successful
    if response.status_code == 200:
        # Parse the JSON data from the response
        data = response.json()

        # Extract the relevant information from the data
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Return the weather information as a tuple
        return (temperature, humidity, wind_speed)
    else:
        # If the API request was not successful, return an error message
        return "Error: Could not retrieve weather data."


if __name__ == "__main__":
    # Get the city name and API key from the user
    city_name = input("Enter city name: ")
    api_key = "5152731c5f39beda8451a898b85d55dc"

    # Call the get_weather function and store the result in a variable
    weather_data = get_weather(city_name, api_key)

    # Check if the weather data is a tuple (i.e. the API request was successful)
    if type(weather_data) == tuple:
        # Print the weather information
        print("Temperature: {:.1f}°C".format(weather_data[0] - 273.15))
        print("Humidity: {}%".format(weather_data[1]))
        print("Wind Speed: {:.1f} m/s".format(weather_data[2]))

    else:
        # If the weather data is not a tuple, it's an error message
        print("API request failed with status code:", response.status_code)
        print("Response content:", response.content)
        print(weather_data)
