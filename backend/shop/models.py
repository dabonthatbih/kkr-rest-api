from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

RATINGS = [
			(1,'1'),
			(2,'2'),
			(3,'3'),
			(4,'4'),
			(5,'5'),

]
# Create your models here.
class products(models.Model):
	id = models.CharField(max_length=100, primary_key=True)
	product = models.CharField(max_length=100, unique=True)
	description = models.CharField(max_length=1000)
	price_now = models.CharField(max_length=20)
	price_before = models.CharField(max_length=20)
	model = models.CharField(max_length=200)
	brand = models.CharField(max_length=200)
	category = models.CharField(max_length=200)


class reviews(models.Model):
	product = models.ForeignKey(products, on_delete=models.CASCADE)	
	reviewer = 	models.OneToOneField(User, on_delete=models.CASCADE)
	text = models.CharField(max_length=400)
	#rating 1/5
	rating = models.CharField(max_length=5, choices=RATINGS)
	date = models.DateTimeField(auto_now_add=True)

class reviewerprocon(models.Model):
	review = models.ForeignKey(reviews, on_delete=models.CASCADE)
	pro = models.CharField(max_length=300)
	con = models.CharField(max_length=300)
