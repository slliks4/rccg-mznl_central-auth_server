# Main url Config
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Apps url config
    path('account/', include('apps.account.urls'))
]
