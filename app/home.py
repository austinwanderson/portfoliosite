from framework.request_handler import AndersonRequestHandler
from google.appengine.ext import ndb
import urllib
import json


class Home(AndersonRequestHandler):


	def get(self):
		self.render('homepage/index.html')

class Blog(AndersonRequestHandler):

	def get(self):
		year = self.request.get("y")
   		month = self.request.get("m")
   		day = self.request.get("d")
   		print(year)
   		print(month)
   		print(day)
   		if not day == "" and not month == "" and not year == "":
   			url = "blog/posts/" + year + "/" + month + "/" + day + ".html"

   		else:
   			url = "blog/blog.html"

		self.render(url)

class Portfolio(AndersonRequestHandler):

	def get(self):
		self.render('portfolio/portfolio.html')

class GeoView(AndersonRequestHandler):

	def get(self):
		self.render('portfolio/geoview.html')

class AutoGIS(AndersonRequestHandler):

	def get(self):
		self.render('portfolio/autogis.html')

class SmartDisplay(AndersonRequestHandler):

	def get(self):
		self.render('portfolio/smartdisplay.html')

class EDIS(AndersonRequestHandler):

	def get(self):
		self.render('portfolio/edis.html')

class AWA(AndersonRequestHandler):

	def get(self):
		self.render('portfolio/awa.html')

class Contact(AndersonRequestHandler):

	def get(self):
		self.render('contact/contact.html')

class Thanks(AndersonRequestHandler):

	def get(self):
		self.render('contact/thank-you.html')
