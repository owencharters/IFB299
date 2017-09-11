from django.db import models

class City(models.Model):
	city_name = models.CharField(max_length=40)

class User(models.Model):
	user_name= models.CharField(max_length=26)
	user_dob = models.DateTimeField('Date of Birth')
	user_type = models.IntegerField(default=1)
	
class UserType(models.Model):
	type_name = models.CharField(max_length=26)
	has_Colleges = models.BooleanField()
	has_Libraries = models.BooleanField()
	has_Industries = models.BooleanField()
	has_Hotels = models.BooleanField()
	has_Parks = models.BooleanField()
	has_Zoos = models.BooleanField()
	has_Museums = models.BooleanField()
	has_Restaurants = models.BooleanField()
	has_Malls = models.BooleanField()
# Create your models here.
