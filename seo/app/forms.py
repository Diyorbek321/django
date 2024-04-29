from django import forms
from .models import EmailSubscriber


class EmailSubscriberForm(forms.ModelForm):
    class Meta:
        model = EmailSubscriber
        fields = ['email']
