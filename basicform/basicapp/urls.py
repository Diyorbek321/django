from django.urls import path
from .views import index, user

urlpatterns = [
    path('', index, name='index'),
    path('users/', user, name='users '),
]
