from django.db import models


class User(models.Model):
	user_id= models.IntegerField(default=1)
	user_type = models.CharField(default=1)
	home_city = models.IntegerField(default=1)
	email = models.CharField(max_length=300)
	password = models.CharField()
	def __str__(self):
		return self.user_type, self.email, self.password

class UserType(models.Model):
	type_id = models.IntegerField(default=1)
	type_desc = models.CharField(max_length=20)
	def __str__(self):
	    return self.type_desc

class Weather(models.Model):
	weather_id = models.IntegerField(default=1)
	weather = models.CharField()
	def __str__(self):
		return self.weather

class Cities(models.Model):
	city_id = models.IntegerField(default=1)
	title = models.CharField(max_length=100)
	weather = models.ForeignKey(Weather)
	def __str__(self):
	    return self.title ,self.weather

class Libraries(models.Model):
	library_id = models.IntegerField(default=1)
	city = models.ForeignKey(Cities)
	library_name = models.CharField(max_length=100)
	phone_number = models.CharField()
	address = models.CharField(max_length=300)
	email = models.CharField(max_length=60)
	def __str__(self):
	    return self.library_name, self.phone_number, self.address, self.email self.city

class Colleges(models.Model):
	college_id = models.IntegerField(default=1)
	city = models.ForeignKey(Cities)
	college_name = models.CharField(max_length=100)
	phone_number = models.CharField()
	address = models.CharField(max_length=300)
	def __str__(self):
	    return self.college_name, self.phone_number, self.address, self.city

class Departments(models.Model):
	department_id = models.IntegerField(default=1)
	description = models.CharField()
	college = models.ForeignKey(Colleges)
	def __str__(self):
	    return self.description, self.college

class Industries(models.Model):
	industry_id = models.IntegerField(default=1)
	city = models.ForeignKey(Cities)
	college = models.ForeignKey(Colleges)
	phone_number = models.CharField()
	address = models.CharField(max_length=300)
	def __str__(self):
	    return self. city, self.college, self.phone_number, self.address

class IndustryType(models.Model):
	type_id = models.IntegerField(default=1)
	description = models.CharField()
	Industry = models.ForeignKey(Industries)
	def __str__(self):
	    return self.description, self.Industry

class Parks(models.Model):
	park_id = models.IntegerField(default=1)
	park_name = models.CharField()
	city = models.ForeignKey(Cities)
	phone_number = models.CharField()
	address = models.CharField(max_length=300)
	email= models.CharField(max_length=60)
	def __str__(self):
	    return self.park_name, self.city, self.phone_number, self.address, self.email

class Hotels(models.Model):
	hotel_id = models.IntegerField(default=1)
	hotel_name = models.CharField()
	city = models.ForeignKey(Cities)
	phone_number = models.CharField()
	address = models.CharField(max_length=300)
	email= models.CharField(max_length=60)
	def __str__(self):
	    return self.hotel_name, self.city, self.phone_number, self.address, self.email

class Museums(models.Model):
	museum_id = models.IntegerField(default=1)
	museum_name = models.CharField()
	city = models.ForeignKey(Cities)
	phone_number = models.CharField()
	address = models.CharField(max_length=300)
	email= models.CharField(max_length=60)
	def __str__(self):
	    return self.museum_name, self.city, self.phone_number, self.address, self.email

class Zoos(models.Model):
	zoo_id = models.IntegerField(default=1)
	zoo_name = models.CharField()
	city = models.ForeignKey(Cities)
	phone_number = models.CharField()
	address = models.CharField(max_length=300)
	email= models.CharField(max_length=60)
	def __str__(self):
	    return self.zoo_name, self.city, self.phone_number, self.address, self.email

class Malls(models.Model):
	mall_id = models.IntegerField(default=1)
	mall_name = models.CharField()
	city = models.ForeignKey(Cities)
	phone_number = models.CharField()
	address = models.CharField(max_length=300)
	email= models.CharField(max_length=60)
	def __str__(self):
	    return self.mall_name, self.city, self.phone_number, self.address, self.email

class Restaurants(models.Model):
	restaurant_id = models.IntegerField(default=1)
	restaurant_name = models.CharField()
	city = models.ForeignKey(Cities)
	phone_number = models.CharField()
	address = models.CharField(max_length=300)
	email= models.CharField(max_length=60)
	def __str__(self):
	    return self.restaurant_name, self.city, self.phone_number, self.address, self.email
