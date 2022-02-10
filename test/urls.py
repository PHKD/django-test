import imp
from socket import INADDR_MAX_LOCAL_GROUP
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]
