from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from app.forms import EmailSubscriberForm
from app.models import EmailSubscriber


# Create your views here.
class HomePageTemplateView(TemplateView):
    template_name = 'index.html'


def subscribe(request):
    if request.method == 'POST':
        form = EmailSubscriberForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save()
            EmailSubscriber.objects.all(email=email)
            return HttpResponseRedirect('/')
    else:
        form = EmailSubscriberForm()
    return render(request, 'index.html', {'form': form})
