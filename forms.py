from django import forms
from django.forms import ModelForm
from app.models import ContactModel

class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = ('first_name','email','subject','message')