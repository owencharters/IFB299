from django.db import models
from django.contrib.auth.models import User


class User(models.Model):

	user_id= models.AutoField(primary_key=True)

	username= models.CharField(max_length=20)

	user_firstname =  models.CharField(max_length=20, blank=True, null=True)

	user_lastname = models.CharField(max_length=20, blank=True, null=True)

	user_type = models.CharField(max_length=20)

	home_city = models.IntegerField(default=1)

	email = models.CharField(max_length=300, blank=True, null=True)

	password = models.CharField(max_length=50)

	def __str__(self):

		return self.username
	def __str__(self):

		return self.user_lastname


class UserType(models.Model):

	type_id = models.AutoField(primary_key=True)

	type_desc = models.CharField(max_length=30)

	def __str__(self):

		return self.type_desc



class Weather(models.Model):

	weather_id = models.AutoField(primary_key=True)

	weather = models.CharField(max_length=50)

	def __str__(self):

		return self.weather



class Cities(models.Model):

	city_id = models.AutoField(primary_key=True)

	title = models.CharField(max_length=100)

	weather = models.ForeignKey(Weather)

	def __str__(self):

		return self.title



class Libraries(models.Model):

	library_id = models.AutoField(primary_key=True)

	city = models.ForeignKey(Cities)

	library_name = models.CharField(max_length=100)

	phone_number = models.CharField(max_length=10)

	address = models.CharField(max_length=300)

	email = models.CharField(max_length=60)

	def __str__(self):

		return self.library_name





class Colleges(models.Model):

	college_id = models.AutoField(primary_key=True)

	city = models.ForeignKey(Cities)

	college_name = models.CharField(max_length=100)

	phone_number = models.CharField(max_length=10)

	address = models.CharField(max_length=300)

	def __str__(self):

		return self.college_name





class Departments(models.Model):

	department_id = models.AutoField(primary_key=True)

	description = models.CharField(max_length=10)

	college = models.ForeignKey(Colleges)

	def __str__(self):

		return self.description



class Industries(models.Model):

	industry_id = models.AutoField(primary_key=True)

	city = models.ForeignKey(Cities)

	name = models.CharField(max_length=40)

	phone_number = models.CharField(max_length=10)

	address = models.CharField(max_length=300)

	def __str__(self):

		return self.name



class IndustryType(models.Model):

	type_id = models.AutoField(primary_key=True)

	description = models.CharField(max_length=100)



	def __str__(self):

		return self.description

class Parks(models.Model):

	park_id = models.AutoField(primary_key=True)

	park_name = models.CharField(max_length=100)

	city = models.ForeignKey(Cities)

	phone_number = models.CharField(max_length=10)

	address = models.CharField(max_length=300)

	email= models.CharField(max_length=60)

	def __str__(self):

		return self.park_name



class Hotels(models.Model):

	hotel_id = models.AutoField(primary_key=True)

	hotel_name = models.CharField(max_length=100)

	city = models.ForeignKey(Cities)

	phone_number = models.CharField(max_length=10)

	address = models.CharField(max_length=300)

	email= models.CharField(max_length=60)

	def __str__(self):

		return self.hotel_name

class Museums(models.Model):

	museum_id = models.AutoField(primary_key=True)

	museum_name = models.CharField(max_length=100)

	city = models.ForeignKey(Cities)

	phone_number = models.CharField(max_length=10)

	address = models.CharField(max_length=300)

	email= models.CharField(max_length=60)

	def __str__(self):

		return self.museum_name

class Zoos(models.Model):

	zoo_id = models.AutoField(primary_key=True)

	zoo_name = models.CharField(max_length=100)

	city = models.ForeignKey(Cities)

	phone_number = models.CharField(max_length=10)

	address = models.CharField(max_length=300)

	email= models.CharField(max_length=60)

	def __str__(self):

		return self.zoo_name



class Malls(models.Model):

	mall_id = models.AutoField(primary_key=True)

	mall_name = models.CharField(max_length=100)

	city = models.ForeignKey(Cities)

	phone_number = models.CharField(max_length=10)

	address = models.CharField(max_length=300)

	email= models.CharField(max_length=60)

	def __str__(self):

		return self.mall_name



class Restaurants(models.Model):

	restaurant_id = models.AutoField(primary_key=True)

	restaurant_name = models.CharField(max_length=100)

	city = models.ForeignKey(Cities)

	phone_number = models.CharField(max_length=10)

	address = models.CharField(max_length=300)

	email= models.CharField(max_length=60)

	def __str__(self):

		return self.restaurant_name

class Document(models.Model):
	description = models.CharField(max_length=255, blank=True)
	document = models.FileField(upload_to='')
	uploaded_at = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	type_id = models.ForeignKey(UserType, default=2)

	city_id = models.ForeignKey(Cities, default=2)

	def User(self):

		return self.user
