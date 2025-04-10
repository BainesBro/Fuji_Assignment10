# File Name: main.py
# Student Name: Collin Baines / Vanshika Rana
# email: bainesct@mail.uc.edu, ranava@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 04/10/2025
# Course #/Section: IS4010-002
# Semester/Year: Spring/2025
# Brief Description of the assignment: This assignment is meant to familiarize us with API's and manipulating data with them.
# Brief Description of what this module does: This module creates functions that allow us to manipulate data in our chosen API.
# Citations: https://openweathermap.org/current , https://home.openweathermap.org/api_keys
# Anything else that's relevant: N/A

from weatherPackage.weather import WeatherHandler

def main():
    """
    Main method to execute the weather fetch, display and save process.
    """
    city = "Cincinnati"
    api_key = "4af0ee1266df398eaa3e808679c2e4a8"  #OpenWeather API key

    try:
        handler = WeatherHandler(city, api_key)

        #Call API
        json_data = handler.fetch_weather()

        #Parse important data
        parsed = handler.parse_weather(json_data)

        #Display to console
        print("Weather Report:")
        for key, value in parsed.items():
            print(f"{key}: {value}")

        #Save to CSV
        handler.save_to_csv(parsed)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
   
