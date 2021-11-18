from django.urls import path
from . import views

urlpatterns = [
     path('', views.find_by_map_page.as_view(), name='find_by_map_page'),
     path('find/by/name', views.find_by_name_page.as_view(), name='find_by_name_page'),
     path('find/by/list', views.location_list_page.as_view(), name='location_list_page'),
     path('find/by/coordinates',views.find_by_coordinates,  name='find_by_coordinates'),
]