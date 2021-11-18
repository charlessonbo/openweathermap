from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from django.shortcuts import render


class ExceptionMiddleware(MiddlewareMixin):

    def process_request(self, request):
        response = self.get_response(request)

        if response.status_code == 404 and "Page not found" in str(response.content):
           return render(request, '404.html')
        
        if response.status_code == 500:
           return render(request, '500.html')

        return response