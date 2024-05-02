from django import forms
from django.core import validators
from .models import User


# def check_for_z(value):
#     if value[0].lower() !='z':
#         raise forms.ValidationError('NEEDS TO START WITH Z')
# class FormName(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     verify_email = forms.EmailField(label='enter your email again')
#     text = forms.CharField(widget=forms.Textarea)
#     # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
#     #                              validators=[validators.MaxLengthValidator(0)])
#
#     def clean(self):
#         all_clean_data = super().clean()
#         email = all_clean_data['email']
#         cerify_email = all_clean_data['verify_email']
#
#         if email != cerify_email:
#             raise forms.ValidationError('Make sure emails match!')

class NewUserForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    class Meta:
        model = User
        fields = '__all__'
