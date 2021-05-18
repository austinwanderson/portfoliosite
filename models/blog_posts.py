from google.appengine.ext import ndb
from hashlib import sha256
from base64 import b64encode
from os import urandom
import uuid

class BlogPost(ndb.Model):
	author = ndb.StringProperty(required=True)
	date = ndb.DateTimeProperty(required=True)
	content = ndb.TextProperty(required=True)
	comments = ndb.ListProperty(required=True)
	
	
#	@classmethod
#	def check_if_exists(cls, email):
#		return cls.query(cls.email == email).get()
#	
#	@classmethod
#	def add_new_user(cls, name, email, password):
#		user = cls.check_if_exists(email)
#		
#		if not user:
#			
#			random_bytes = urandom(64)
#			salt = b64encode(random_bytes).decode('utf-8')
#			hashed_password = salt + sha256(salt + password).hexdigest()
#			
#			confirmation_code = str(uuid.uuid4().get_hex())
#			
#			new_user_key = cls(
#				name=name,
#				email=email,
#				password=hashed_password,
#				confirmation_code=confirmation_code
#			).put()
#			
#			print new_user_key
#			
#			return {
#				'created':True,
#				'user_id':new_user_key.id(),
#				'confirmation_code':confirmation_code
#			}
#
#		else: 
#			return {
#				'created':False,
#				'title':'This email is already in use',
##				'message':'Please log in if this is your email account.'
#			}