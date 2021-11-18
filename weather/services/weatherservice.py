import requests
from django.conf import settings
from weatherapp.utils import *

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

    results['location_name'] = data['name']    
    results['date_time'] = get_date_now()
    results['temperature'] = change_format_temperature(data['main']['temp']) 
    results['weather_description'] = change_format_to_title(data['weather'][0]['description'])
    results['wind'] = change_format_wind(data['wind']['speed'])
    results['humidity'] = change_format_humidity(data['main']['humidity'])

    return generate_api_response(
        message='success',
        result=results,
        status_code=api_response.status_code
    )
