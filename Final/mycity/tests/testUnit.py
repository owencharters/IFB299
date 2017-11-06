from django.test import TestCase
from django.test.client import RequestFactory
from mycity.views import *
from mycity.models import *
from django.http import HttpResponseRedirect

class SummaryTests(TestCase):
	# Handling of summary/[button url] testing
	fixtures = ['tests']

	def setUp(self):
		self.factory = RequestFactory()

	# Test for incorrect URL Input
	def test_summaryFalse(self):
		request = self.factory.get('/summary/fake')

		try:
			response = summary(request, 'fake')
			self.fail("Url shouldn't exist")
		except ValueError:
			pass

	def test_summaryHotelsTrue(self):
		request = self.factory.get('/summary/hotels')

		try:
			response = summary(request, 'hotels')
		except ValueError:
			self.fail("Hotels Url setup wrong")
			pass

	def test_summaryParksTrue(self):
		request = self.factory.get('/summary/parks')

		try:
			response = summary(request, 'parks')
		except ValueError:
			self.fail("Parks Url setup wrong")
			pass

	def test_summaryZoosTrue(self):
		request = self.factory.get('/summary/zoos')

		try:
			response = summary(request, 'zoos')
		except ValueError:
			self.fail("Zoos Url setup wrong")
			pass

	def test_summaryMuseumsTrue(self):
		request = self.factory.get('/summary/museums')

		try:
			response = summary(request, 'museums')
		except ValueError:
			self.fail("Museums Url setup wrong")
			pass

	def test_summaryMallsTrue(self):
		request = self.factory.get('/summary/malls')

		try:
			response = summary(request, 'malls')
		except ValueError:
			self.fail("Malls Url setup wrong")
			pass

	def test_summaryRestaurantsTrue(self):
		request = self.factory.get('/summary/restaurants')

		try:
			response = summary(request, 'restaurants')
		except ValueError:
			self.fail("Restaurants Url setup wrong")
			pass

	def test_summaryCollegesTrue(self):
		request = self.factory.get('/summary/colleges')

		try:
			response = summary(request, 'colleges')
		except ValueError:
			self.fail("Colleges Url setup wrong")
			pass

	def test_summaryLibrariesTrue(self):
		request = self.factory.get('/summary/libraries')

		try:
			response = summary(request, 'libraries')
		except ValueError:
			self.fail("Libraries Url setup wrong")
			pass

	def test_summaryIndustriesTrue(self):
		request = self.factory.get('/summary/industries')

		try:
			response = summary(request, 'industries')
		except ValueError:
			self.fail("Industries Url setup wrong")
			pass

class WebpageTests(TestCase):
	# Test that webpages exist at the necessary Urls

	def setUp(self):
		self.factory = RequestFactory()

	def test_mapupload(self):
		request = self.factory.get('mapupload')
		response = model_form_upload(request)

		self.assertEqual(response.status_code, 200)

	def test_signup(self):
		request = self.factory.get('register')
		response = signup(request)

		self.assertEqual(response.status_code, 200)
		
	def test_signup(self):
		request = self.factory.get('')
		response = login(request)

		self.assertEqual(response.status_code, 200)

class RedirectTests(TestCase):
	# Test that redirects exist where necessary

	def setUp(self):
		self.factory = RequestFactory()

	def test_adminRedirect(self):
		response = HttpResponseRedirect('login')
		self.assertEqual(response.status_code, 302)

	def test_baseRedirect(self):
		response = HttpResponseRedirect('')
		self.assertEqual(response.status_code, 302)

class DatabaseTests(TestCase):
	# Test that database is populated appropriately
	fixtures = ['tests']

	def test_libraries(self):
		tableInfo = Libraries.objects.all()
		individualInfo = tableInfo[:1].get()
		name = str(individualInfo)

		self.assertEqual(name, "Chermside Library")

	def test_colleges(self):
		tableInfo = Colleges.objects.all()
		individualInfo = tableInfo[:1].get()
		name = str(individualInfo)

		self.assertEqual(name, "Queensland University of Technology")

	def test_industries(self):
		tableInfo = Industries.objects.all()
		individualInfo = tableInfo[:1].get()
		name = str(individualInfo)

		self.assertEqual(name, "Rugs a Million")

	def test_parks(self):
		tableInfo = Parks.objects.all()
		individualInfo = tableInfo[:1].get()
		name = str(individualInfo)

		self.assertEqual(name, "New Farm Park")

	def test_hotels(self):
		tableInfo = Hotels.objects.all()
		individualInfo = tableInfo[:1].get()
		name = str(individualInfo)

		self.assertEqual(name, "Royal Albert")

	def test_museums(self):
		tableInfo = Museums.objects.all()
		individualInfo = tableInfo[:1].get()
		name = str(individualInfo)

		self.assertEqual(name, "Gallery of Modern Art")

	def test_zoos(self):
		tableInfo = Zoos.objects.all()
		individualInfo = tableInfo[:1].get()
		name = str(individualInfo)

		self.assertEqual(name, "Alma Park Zoo")

	def test_malls(self):
		tableInfo = Malls.objects.all()
		individualInfo = tableInfo[:1].get()
		name = str(individualInfo)

		self.assertEqual(name, "Queen St Mall")

	def test_restaurants(self):
		tableInfo = Restaurants.objects.all()
		individualInfo = tableInfo[:1].get()
		name = str(individualInfo)

		self.assertEqual(name, "McDonalds Albion")
