import requests
import os
from datetime import datetime
from django.conf import settings
from weatherapp.middleware import get_response


def weather_by_coordinates(latitude,longitude):
    url= f"{settings.OPEN_WEATHER_MAP_API}?lat={latitude}&lon={longitude}&appid={settings.OPEN_WEATHER_MAP_API_KEY}"
    response = requests.get(url)
    return generate_api_response(response)


def weather_by_name(name):
    url= f"{settings.OPEN_WEATHER_MAP_API}?q={name}&appid={settings.OPEN_WEATHER_MAP_API_KEY}"
    response = requests.get(url)
    return generate_api_response(response)


def generate_api_response(response):
    if response.status_code == 200:
        return generate_weather_forecast(response)
    else:
        return generate_error_message(response)


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

    return get_response(
        message='success',
        result=results,
        status_code=api_response.status_code
    )


def generate_error_message(api_response):
    data = api_response.json()
    return get_response(
        message=data['message'],
        result={},
        status_code=api_response.status_code
    )