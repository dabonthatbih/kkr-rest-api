from django.db import models
from django.contrib.auth.models import User

INOROUTS = [('in','in'),
			('out','out'),]
# Create your models here.
class wallet(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	balance = models.DecimalField(max_digits = 1000000000, decimal_places = 2)
	accountnumber = models.IntegerField(unique=True)
	opendate = models.DateTimeField(auto_now_add=True)

class transactions(models.Model):
	wallet = models.ForeignKey(User, on_delete=models.CASCADE)
	inorout = models.CharField(max_length=30, choices=INOROUTS)
	amount = models.DecimalField(max_digits = 1000000000,decimal_places=2)
	receiver = models.CharField(max_length=100)
	date = models.DateTimeField(auto_now_add=True)