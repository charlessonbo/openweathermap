import requests
import os
from datetime import datetime
from django.conf import settings

def weather_by_coordinates(latitude,longitude):
    url= f"{settings.OPEN_WEATHER_MAP_API_BY_COORDINATES}?lat={latitude}&lon={longitude}&appid={settings.OPEN_WEATHER_MAP_API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return generate_weather_forecast(response.json())
    else:
        return generate_error_message(response.json())


def generate_weather_forecast(data):
    response = {}

    temperature = ((data['main']['temp']) - 273.15)
    weather_description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    location_name = data['name']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    response['temperature'] = "{:.2f}°C".format(temperature)
    response['wind'] = f"{wind}'kmph"
    response['humidity'] = f"{humidity}%"
    response['weather_description'] = str(weather_description).title()
    response['location_name'] = location_name
    response['date_time'] = date_time

    return response


def generate_error_message(data):
    response = {}
    response['message'] = data['message']
    response['status'] = data['cod']
    return response