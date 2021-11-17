from django.shortcuts import render
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import service
from .forms import WeatherForm



from django.views import View

class index(View):
    def get(self, request):
        context ={}
        form = WeatherForm()
        context['form']= form

        return render(
            request,
            'weather/index.html',
            context,
        )

    def post(self, request):
        result = None
        context ={}
        form = WeatherForm(request.POST)
        context['form']= form

        if form.is_valid():
            response = service.weather_by_name(form.cleaned_data['location'])
            if response['status_code'] == 200:
                context['result']= response["result"]

        return render(
            request,
            'weather/index.html',
            context
        )
      

def get_weather_by_coordinates(request):
    response = service.weather_by_coordinates(request.GET['latitude'], request.GET['longitude'])
    return JsonResponse(response)