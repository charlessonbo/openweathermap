import requests
import os
from datetime import datetime
from django.conf import settings
from weatherapp.utils import generate_error_api_response

def weather_by_coordinates(latitude,longitude):
    url= f"{settings.OPEN_WEATHER_MAP_API}?lat={latitude}&lon={longitude}&appid={settings.OPEN_WEATHER_MAP_API_KEY}"
    response = requests.get(url)
    return generate_weather_api_response(response, f"latitude: {latitude} longitude: {longitude}")


def weather_by_name(name):
    url= f"{settings.OPEN_WEATHER_MAP_API}?q={name}&appid={settings.OPEN_WEATHER_MAP_API_KEY}"
    response = requests.get(url)
    return generate_weather_api_response(response, f"name {name}")


def generate_weather_api_response(response, input_data):
    if not response.status_code == 200:
        return generate_error_api_response(response, input_data)
    
    return generate_weather_forecast(response)
        

def generate_weather_forecast(api_response):
    data = api_response.json()
    results = {}

    temperature = ((data['main']['temp']) - 273.15)
    weather_description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    location_name = data['name']
    date_time = datetime.now().strftime("%b %d %Y | %I:%M:%S %p")

    results['temperature'] = "{:.2f}°C".format(temperature)
    results['wind'] = f"{wind} kmph"
    results['humidity'] = f"{humidity}%"
    results['weather_description'] = str(weather_description).title()
    results['location_name'] = location_name
    results['date_time'] = date_time

    return {
        "message": 'success',
        "result": results,
        "status_code": api_response.status_code
    }
