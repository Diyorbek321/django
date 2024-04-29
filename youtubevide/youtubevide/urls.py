
from django.contrib import admin
from django.urls import path
from .views import youtube

urlpatterns = [
    path('admin/', admin.site.urls),
    path('youtube/',youtube)
]
