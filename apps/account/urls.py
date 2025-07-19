# Account url config
from django.urls import path

from apps.account.views import UserRetrieveAPIView

urlpatterns = [
    path(
        'me',  # route
        UserRetrieveAPIView.as_view(),  # view
        name='user-detail'  # name
    ),
]
