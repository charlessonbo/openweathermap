from django.urls import path
from . import views

urlpatterns = [
     path('', 
          views.find_by_map.as_view(), 
          name='find_by_map'),

     path('find/by/name', 
         views.find_by_name.as_view(), 
         name='find_by_name'),

     path('get/location/weather',
          views.get_weather_by_coordinates, 
          name='get_weather_by_coordinates')  
]