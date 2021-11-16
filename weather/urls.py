from django.urls import path
from . import views

urlpatterns = [
    path('', 
         views.index, 
         name='index'),

    path('/get/location/weather',
         views.get_weather_by_coordinates, 
         name='get_weather_by_coordinates')  
]