import requests
import os
from datetime import datetime
from django.conf import settings

def weather_by_coordinates(latitude,longitude):
    url= f"{settings.OPEN_WEATHER_MAP_API}?lat={latitude}&lon={longitude}&appid={settings.OPEN_WEATHER_MAP_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        return generate_weather_forecast(response)
    else:
        return generate_error_message(response)


def generate_weather_forecast(api_response):
    data = api_response.json()
    response = { 'data':{} }

    temperature = ((data['main']['temp']) - 273.15)
    weather_description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    location_name = data['name']
    date_time = datetime.now().strftime("%b %d %Y | %I:%M:%S %p")

    response['data']['temperature'] = "{:.2f}°C".format(temperature)
    response['data']['wind'] = f"{wind} kmph"
    response['data']['humidity'] = f"{humidity}%"
    response['data']['weather_description'] = str(weather_description).title()
    response['data']['location_name'] = location_name
    response['data']['date_time'] = date_time
    response['message'] = 'success'
    response['status_code'] = api_response.status_code
    return response


def generate_error_message(api_response):
    data = api_response.json()
    response = {}
    response['message'] = data['message']
    response['status_code'] = api_response.status_code
    return response