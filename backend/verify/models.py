from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

genders = [('M','Male'),
			('F','Female')]


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=200,choices = genders)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = CountryField()
    adress = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=20)

