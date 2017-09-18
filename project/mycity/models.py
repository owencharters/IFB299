from django.db import models

class User(models.Model):
	user_id= models.IntegerField(default=1)
	user_type = models.CharField(max_length=20)
	home_city = models.IntegerField(default=1)
	email = models.CharField(max_length=300)
	password = models.CharField(max_length=50)

class UserType(models.Model):
	type_id = models.IntegerField(default=1)
	type_desc = models.CharField(max_length=30)

class Weather(models.Model):
	weather_id = models.IntegerField(default=1)
	weather = models.CharField(max_length=50)

class Cities(models.Model):
	city_id = models.IntegerField(default=1)
	title = models.CharField(max_length=100)
	weather = models.ForeignKey(Weather)

class Libraries(models.Model):
	library_id = models.IntegerField(default=1)
	city = models.ForeignKey(Cities)
	library_name = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=10)
	address = models.CharField(max_length=300)
	email = models.CharField(max_length=60)


class Colleges(models.Model):
	college_id = models.IntegerField(default=1)
	city = models.ForeignKey(Cities)
	college_name = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=10)
	address = models.CharField(max_length=300)


class Departments(models.Model):
	department_id = models.IntegerField(default=1)
	description = models.CharField(max_length=10)
	college = models.ForeignKey(Colleges)

class Industries(models.Model):
	industry_id = models.IntegerField(default=1)
	city = models.ForeignKey(Cities)
	college = models.ForeignKey(Colleges)
	phone_number = models.CharField(max_length=10)
	address = models.CharField(max_length=300)

class IndustryType(models.Model):
	type_id = models.IntegerField(default=1)
	description = models.CharField(max_length=100)
	Industry = models.ForeignKey(Industries)

class Parks(models.Model):
	park_id = models.IntegerField(default=1)
	park_name = models.CharField(max_length=100)
	city = models.ForeignKey(Cities)
	phone_number = models.CharField(max_length=10)
	address = models.CharField(max_length=300)
	email= models.CharField(max_length=60)

class Hotels(models.Model):
	hotel_id = models.IntegerField(default=1)
	hotel_name = models.CharField(max_length=100)
	city = models.ForeignKey(Cities)
	phone_number = models.CharField(max_length=10)
	address = models.CharField(max_length=300)
	email= models.CharField(max_length=60)

class Museums(models.Model):
	museum_id = models.IntegerField(default=1)
	museum_name = models.CharField(max_length=100)
	city = models.ForeignKey(Cities)
	phone_number = models.CharField(max_length=10)
	address = models.CharField(max_length=300)
	email= models.CharField(max_length=60)

class Zoos(models.Model):
	zoo_id = models.IntegerField(default=1)
	zoo_name = models.CharField(max_length=100)
	city = models.ForeignKey(Cities)
	phone_number = models.CharField(max_length=10)
	address = models.CharField(max_length=300)
	email= models.CharField(max_length=60)

class Malls(models.Model):
	mall_id = models.IntegerField(default=1)
	mall_name = models.CharField(max_length=100)
	city = models.ForeignKey(Cities)
	phone_number = models.CharField(max_length=10)
	address = models.CharField(max_length=300)
	email= models.CharField(max_length=60)

class Restaurants(models.Model):
	restaurant_id = models.IntegerField(default=1)
	restaurant_name = models.CharField(max_length=100)
	city = models.ForeignKey(Cities)
	phone_number = models.CharField(max_length=10)
	address = models.CharField(max_length=300)
	email= models.CharField(max_length=60)
