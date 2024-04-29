from django.urls import path
from app.views import HomePageTemplateView,subscribe

urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='home_page'),
    path('subscribe/',subscribe,name='subscribe')
]
