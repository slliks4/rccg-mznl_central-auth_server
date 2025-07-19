# apps/auth/urls.py
from django.urls import path

# Simple JWT's Token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

from apps.auth.views.registration import registration_confirm

# Urls pattern
urlpatterns = [
    # Token (simple_jwt)
    path(
        'token/',  # route
        TokenObtainPairView.as_view(),  # view
        name='token_obtain_pair'  # name
    ),
    path(
        'token/refresh/',  # route
        TokenRefreshView.as_view(),  # view
        name='token_refresh'  # name
    ),
    path(
        'token/verify/',  # route
        TokenVerifyView.as_view(),  # view
        name='token_verify'  # name
    ),

    # Registration
    path(
        'registration/confirm',  # route
        registration_confirm,  # view
        name='registration_confirm'  # name
    ),
]
