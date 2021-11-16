from django.shortcuts import render
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'weather/bymaptemplates/index.html')


def get_weather_by_coordinates(request):
    print("HEREH RHEHRH HERH HERH")
    response = {}
    response['result'] = 'error'
    response['message'] = 'Some error message'

    return JsonResponse({"valid":True}, status = 200)