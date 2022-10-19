# Introduction to APIs in Python
# Build a weather look-up app with Python and an API from openweathermap.com
# Code based off of/adapted from a YouTube tutorial produced by LeMaster Tech at this link: https://youtu.be/kLNtdehfNrI.
# Here is a good YouTube tutorial on how to hide API keys: https://youtu.be/YdgIWTYQ69A

# Import the necessary modules
import requests
import time
import os
from dotenv import load_dotenv
load_dotenv()

api_key = ""  # Replace this value with your own API key from openweathermap.com.

city_name_state = input('Enter a city and state: ')  # create a variable to store the city name
zip_code = input('Enter the city zip code: ')  # create a variable to store the zip code
country = 'US'  # input('Enter your country code:') # create a variable to store the country code
link_state = f'https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country}&appid={os.getenv("api_key")}&units=imperial'  # create a variable to store the link to the API
response = requests.get(link_state).json()  # create a variable to store the response from the API

# print(response)  # uncomment to see the JSON response

current_temp = response['main']['temp']  # create a variable to store the current temperature
feels_like = response['main']['feels_like']  # create a variable to store what it feels like outside
temp_min = response['main']['temp_min']  # create a variable to store the low temperature
temp_max = response['main']['temp_max']  # create a variable to store the high temperature
humidity = response['main']['humidity']  # create a variable to store the humidity level
sunrise = response['sys']['sunrise']  # create a variable to store the sunrise time
sunset = response['sys']['sunset']  # create a variable to store the sunset time
sunrise_time_val = time.strftime('%#I:%M %p', time.localtime(
    sunrise))  # The "#" is to remove the leading 0 from the time.  Time has been converted from Unix/Epoch time to standard time.
sunset_time_val = time.strftime('%#I:%M %p', time.localtime(sunset))

print(f' - At the location: {city_name_state}, the temperature is currently {current_temp} Fahrenheit.')
print(f' - It currently feels like {feels_like}, with a humidity level of {humidity}%.')
print(f' - The high today in {city_name_state} will be {temp_max}, and the low will be {temp_min}.')
print(f' - The sun will set today at {sunset_time_val}, and the sun will rise tomorrow at {sunrise_time_val}.')
