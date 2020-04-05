# -*- coding: utf-8 -*-
import requests
import json

class Resource(object):
	"""Generic Resource Class"""
	def __init__(self, session, endpoint):
		super(Resource, self).__init__()
		self.session = session
		self.endpoint = endpoint
	
	def loadFromAPI(self, **kwargs):
		"""Calls the API and returns a dictionary of the response"""
		response_dict = None
		url = self.session.base_url + self.endpoint
		for key, value in kwargs.items():
			if key == 'id':
				url += '/' + value

		response = requests.get(url, headers=self.session.headers)
		if (response.status_code == requests.codes.ok):
			response_dict = json.loads(response.text)
		
		return response_dict



class Idea(Resource):
	"""A Prodpad Idea"""
	
	"""If launched with no ID, then don't query the API"""
	def __init__(self):
		super(Idea, self).__init__(session,"""ideas""")
	
	
	"""If launched with an ID, then query the API for this idea"""
	def __init__(self, id, session):
		super(Idea, self).__init__(session,"""ideas""")
		self.id = id
		idea_dict = self.loadFromAPI(id=id)
		
		if idea_dict is not None:
			self.title = idea_dict['title']
	
	
	"""Human-readable string"""
	def __str__(self):
		idea_string = """Idea: (no title)"""
		
		if self.title is not None:
			idea_string = """Idea: """ + str(self.title)

		return idea_string
	
	


	