# Create a program that fetches and displays the current weather for a given city.
# (Requires: requests library and an API like OpenWeatherMap)

import requests


def get_weather(api_key, city):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print(f"Error: {data['message']}")
            return None

    except requests.ConnectionError:
        print("Connection Error. Please check your internet connection.")
        return None
    except requests.Timeout:
        print("Request Timeout. Please try again later.")
        return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None


def display_weather(weather_data):
    if weather_data:
        print("\nWeather Checker:")
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description']}")
    else:
        print("Weather data not available.")


def main():
    API_KEY = "f3136f08ffdacedba4fd6bc50c5a5e9f"
    city = input("Enter the city name: ")

    weather_data = get_weather(API_KEY, city)

    if weather_data:
        display_weather(weather_data)


if __name__ == "__main__":
    main()
