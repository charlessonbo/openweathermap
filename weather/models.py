from django.db import models
from .services import weatherservice


class Location(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    longitude = models.CharField(max_length=30)
    latitude = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    @property
    def weather_forecast(self):
        response = weatherservice.weather_by_name(self.name)
        if response['status_code'] == 200:
            result = response["result"]

        return result
