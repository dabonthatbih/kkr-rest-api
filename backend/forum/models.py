from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class topics(models.Model):
	creater = models.ForeignKey(User, on_delete=models.CASCADE)
	topic = models.CharField(max_length=300)
	name = models.CharField(max_length=100)
	text = models.CharField(max_length=5000000)
	createdate = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)
	closedat = models.DateTimeField(blank=True)

class reactions(models.Model):
	reftopic = models.ForeignKey(topics, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	text = models.CharField(max_length=100)
	createdate = models.DateTimeField(auto_now_add=True)
	