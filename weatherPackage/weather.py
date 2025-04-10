# File Name: weather.py
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

import requests
import csv

class WeatherHandler:
    """
    Handles fetching, parsing, and saving weather data from OpenWeather API.
    """

    def __init__(self, city, api_key):
        self.city = city
        self.api_key = api_key
        self.api_url = (
            f"https://api.openweathermap.org/data/2.5/weather?q={city}"
            f"&appid={api_key}&units=metric"
        )

    def fetch_weather(self):
        """
        Calls OpenWeather API and returns the response as a dictionary.
        """
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"API call failed with status code {response.status_code}")

    def parse_weather(self, data):
        """
        Extracts selected data from the API JSON response.
        """
        parsed = {
            "City": self.city,
            "Temperature (C)": data["main"]["temp"],
            "Humidity (%)": data["main"]["humidity"],
            "Weather Description": data["weather"][0]["description"],
            "Wind Speed (m/s)": data["wind"]["speed"]
        }
        return parsed

    def save_to_csv(self, parsed_data, filename="dataPackage/weather_data.csv"):
        """
        Writes parsed weather data to a CSV file.
        """
        with open(filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=parsed_data.keys())
            writer.writeheader()
            writer.writerow(parsed_data)