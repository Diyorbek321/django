from django.db import models

# Create your models here.
class ContactModel(models.Model):
    first_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=100)
    message = models.TextField()