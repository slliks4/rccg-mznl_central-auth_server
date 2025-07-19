# Account url config
from django.urls import path

from .views import api_endpoints

urlpatterns = [
        path('endpoints', api_endpoints, name='api_endpoints')
]
