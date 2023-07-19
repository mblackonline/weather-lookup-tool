# Introduction to APIs in Python
# Build a weather look-up app with Python and an API from openweathermap.com


# Import the necessary modules
import requests
import time
import os
from dotenv import load_dotenv
from urllib.parse import urlencode

load_dotenv()

# Replace this value with your own API key from openweathermap.com.
api_key = ""

# create a variable to store the city name
city_name_state = input('Enter a city and state: ')
# create a variable to store the zip code
zip_code = input('Enter the city zip code: ')
# input('Enter your country code:') # create a variable to store the country code
country = 'US'

# create a dictionary of parameters to be passed in the URL
payload = {'zip': f'{zip_code},{country}', 'appid': os.getenv("api_key"), 'units': 'imperial'}
# encode the parameters in the URL using urlencode() function from urllib.parse module
url = f'https://api.openweathermap.org/data/2.5/weather?{urlencode(payload)}'

# make a request to the API using the encoded URL
response = requests.get(url).json()

# print(response)  # uncomment to see the JSON response

# create a variable to store the current temperature
current_temp = response['main']['temp']
# create a variable to store what it feels like outside
feels_like = response['main']['feels_like']
# create a variable to store the low temperature
temp_min = response['main']['temp_min']
# create a variable to store the high temperature
temp_max = response['main']['temp_max']
# create a variable to store the humidity level
humidity = response['main']['humidity']
# create a variable to store the sunrise time
sunrise = response['sys']['sunrise']
# create a variable to store the sunset time
sunset = response['sys']['sunset']

# Below, the "#" is to remove the leading 0 from the time.  Time has been converted from Unix/Epoch time to standard time.
sunrise_time_val = time.strftime('%#I:%M %p', time.localtime(sunrise))
sunset_time_val = time.strftime('%#I:%M %p', time.localtime(sunset))

print(f' - At the location: {city_name_state}, the temperature is currently {current_temp} Fahrenheit.')
print(f' - It currently feels like {feels_like}, with a humidity level of {humidity}%.')
print(f' - The high today in {city_name_state} will be {temp_max}, and the low will be {temp_min}.')
print(f' - The sun will set today at {sunset_time_val}, and the sun will rise tomorrow at {sunrise_time_val}.')
