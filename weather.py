# To adjust this code to YOUR city, simply change the city= "name" and replace 'A1C 4H2' in URL with your postal/zip code or your city name.
import requests

city = "St. John's"
url = 'http://api.weatherapi.com/v1/current.json?key=53a2f868208a4dadb29202631251203&q=A1C 4H2&aqi=no'

response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_c')
description = weather_json.get('current').get('condition').get('text')
feels_like = weather_json.get('current').get('feelslike_c')

print("The current weather in", city, "is", description, "and", temp, "C degrees.", "But it feels like the temperature is", feels_like, "C degrees with windchill and/or humidity.")
if (feels_like < 0):
    print("Stay warm out there!")
if (temp > 15.0):
    print("It's a warm one!")
