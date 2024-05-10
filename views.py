

from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from app.forms import ContactForm

# Create your views here.
class HomePageTemplateView(TemplateView):
    template_name = 'index.html'


class AboutPageTemplateView(TemplateView):
    template_name = 'about.html'


class ContactPageTemplateView(ListView):
    template_name = 'contact.html'
    submitted =False
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form=ContactForm
    form = ContactForm
    context_object_name = {'form': form}


class ServicePageTemplateView(TemplateView):
    template_name = 'service.html'


class FeaturePageTemplateView(TemplateView):
    template_name = 'feature.html'


class QuoteTemplateView(TemplateView):
    template_name = 'quote.html'


class TeamTemplateView(TemplateView):
    template_name = 'team.html'


class ErrorPageTemplateView(TemplateView):
    template_name = '404.html'


class TestestimonalPageTemplateView(TemplateView):
    template_name = 'testimonial.html'