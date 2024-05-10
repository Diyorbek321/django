from django.urls import path
from app.views import (HomePageTemplateView,AboutPageTemplateView, ContactPageTemplateView,ServicePageTemplateView,
                       FeaturePageTemplateView, QuoteTemplateView, TeamTemplateView,ErrorPageTemplateView,TestestimonalPageTemplateView)
urlpatterns = [
    path('',HomePageTemplateView.as_view(), name='home_page'),
    path('about/',AboutPageTemplateView.as_view(), name='about_page'),
    path('contact/',ContactPageTemplateView.as_view(),name ='contact_page'),
    path('service/',ServicePageTemplateView.as_view(), name='service_page'),
    path('feature/',FeaturePageTemplateView.as_view(), name='feature_page'),
    path('quote/',QuoteTemplateView.as_view(),name='quote_page'),
    path('team/',TeamTemplateView.as_view(),name='team_page'),
    path('eror/',ErrorPageTemplateView.as_view(),name='eror_page'),
    path('testeminal/',TestestimonalPageTemplateView.as_view(), name='testestimonal_page')
]