from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class City(models.Model):
	name = models.CharField(max_length=255)
	country = models.CharField(max_length=255)
	code = models.CharField(max_length=3)
	def __unicode__(self):
		return self.name
	
	class Meta:
		ordering = ["country"]
		verbose_name_plural = "cities"

class Airport(models.Model):
	city = models.ForeignKey(City)
	code = models.CharField(max_length=255,unique=True)
	def __unicode__(self):
		return self.code

class Booking(models.Model):
	users = models.ManyToManyField(User,null = True)
	reference = models.CharField(max_length=10)
	date_from = models.DateTimeField()
	city = models.ForeignKey(City)
	flight_number = models.CharField(max_length=20)
	def __unicode__(self):
		return self.reference
    