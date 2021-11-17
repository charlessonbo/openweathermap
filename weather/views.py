from django.shortcuts import render
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import service
from .forms import WeatherForm
from django.views import View


class find_by_map(View):
    template = 'weather/findbymap/index.html'
    def get(self, request):
        return render(request, self.template)


class find_by_name(View):
    form = WeatherForm
    template = 'weather/findbyname/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        result = None
        form = self.form(request.POST)

        if form.is_valid():
            response = service.weather_by_name(form.cleaned_data['location'])
            if response['status_code'] == 200:
                result= response["result"]

        return render(request, self.template, {'form': form, 'result': result})


def get_weather_by_coordinates(request):
    response = service.weather_by_coordinates(request.GET['latitude'], request.GET['longitude'])
    return JsonResponse(response)