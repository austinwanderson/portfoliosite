from webapp2 import WSGIApplication
from webapp2 import Route

app = WSGIApplication(
	routes=[
		Route('/', handler='app.home.Home'),
		Route('/contact', handler='app.home.Contact'),
		Route('/portfolio', handler='app.home.Portfolio'),
		Route('/portfolio/geoview', handler='app.home.GeoView'),
		Route('/portfolio/autogis', handler='app.home.AutoGIS'),
		Route('/portfolio/smartdisplay', handler='app.home.SmartDisplay'),
		Route('/portfolio/awa', handler='app.home.AWA'),
		Route('/portfolio/edis', handler='app.home.EDIS'),
		Route('/thanks', handler='app.home.Thanks'),
	]
)
