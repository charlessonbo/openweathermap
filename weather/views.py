from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services import weatherservice
from .forms import WeatherForm
from django.views import View
from django.views.generic.list import ListView
from .models import Location


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
            response = weatherservice.weather_by_name(form.cleaned_data['location'])
            if response['status_code'] == 200:
                result= response["result"]

        return render(request, self.template, {'form': form, 'result': result})


class location_list(ListView):
    model = Location
    template_name='weather/locationlist/list.html'
    paginate_by = 2

def get_weather_by_coordinates(request):
    response = weatherservice.weather_by_coordinates(request.GET['latitude'], request.GET['longitude'])
    return JsonResponse(response)