from django.shortcuts import render
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import service

def index(request):
    return render(request, 'weather/index.html')


def get_weather_by_coordinates(request):
    response = service.weather_by_coordinates(request.GET['latitude'], request.GET['longitude'])
    return JsonResponse(response)