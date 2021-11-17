from django.test import TestCase

from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

from . import views

class UnitTest(SimpleTestCase):

    def test_page_find_by_map_pass(self):
        response = self.client.get(reverse('find_by_map'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather/findbymap/index.html')

    def test_page_find_by_name_pass(self):
        response = self.client.get(reverse('find_by_name'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather/findbyname/index.html')
    
    def test_page_template_404_error_pass(self):
        response = self.client.get('/unknown_page')
        self.assertEquals(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
    
    def test_api_get_weather_by_coordinate_pass(self):
        response = self.client.get('/get/location/weather?latitude=13.63&longitude=93.70')
        data = response.json()
        status_code = data['status_code']
        message = data['message']
        self.assertEquals(response.status_code, 200)
        self.assertEquals(message, 'success')
    
    def test_api_get_weather_by_coordinate_failed(self):
        response = self.client.get('/get/location/weather?latitude=13.63&longitude=9999993.70')
        data = response.json()
        status_code = data['status_code']
        message = data['message']
        self.assertEquals(status_code, 400)
        self.assertEquals(message, 'wrong longitude')

    def test_api_get_weather_by_name_pass(self):
        response = self.client.post("/find/by/name", data={"location": "Manila"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h6 class="flex-grow-1">Manila</h6>', html=True)
    
    def test_api_get_weather_by_name_failed(self):
        response = self.client.post("/find/by/name", data={"location": "UnknownData"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<strong>No available data</strong>', html=True)
   
