# Account url config
from django.urls import path

from apps.account.views import get_user

urlpatterns = [
    path('me', get_user, name='get_user'),
]
