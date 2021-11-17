from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from django.shortcuts import render
import logging

class ExceptionMiddleware(MiddlewareMixin):

    def process_request(self, request):
        response = self.get_response(request)

        if response.status_code == 404 and "Page not found" in str(response.content):
           return render(request, '404.html')
        
        if response.status_code == 500:
           return render(request, '500.html')

        return response
    

def get_response(**kwargs):
    return {
        "message" : kwargs.get('message', None),
        "result" : kwargs.get('result', None),
        "status_code" : kwargs.get('status_code', None),
    }


def log_to_db(message):
    db_logger = logging.getLogger('db')
    db_logger.exception(message)