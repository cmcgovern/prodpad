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
		params = None
		
		url = self.session.base_url + self.endpoint
		for key, value in kwargs.items():
			if key == 'id':
				url += '/' + str(value)
			if key == 'params':
				params = value
			if key == 'add_to_url':
				url += '/' + value

		response = requests.get(url, headers=self.session.headers, params=params)
		if (response.status_code == requests.codes.ok):
			response_dict = json.loads(response.text)
		
		return response_dict


class Idea(Resource):
	"""A Prodpad Idea"""
	
	"""If launched with no ID, then don't query the API"""
	def __init__(self):
		super(Idea, self).__init__(session,"""ideas""")
	
	
	def getFeedback(self):
		"""docstring for getAllFeedback"""
		linked_feedback = []
		
		feedback_items_dict = self.loadFromAPI(id=self.id, add_to_url="""feedback""")
		for feedback_item in feedback_items_dict:
			linked_feedback.append(Feedback(feedback_item, self, self.session))
		
		return linked_feedback
	
	
	"""If launched with an ID, then query the API for this idea"""
	def __init__(self, id, session):
		super(Idea, self).__init__(session,"""ideas""")
		self.short_id = id
		self.options = {'by_project_id': 'true', 'expand': 'true'} # This allows us to use the visible ID to retrieve ideas
		idea_dict = self.loadFromAPI(id=self.short_id, params=self.options)
		
		if idea_dict is not None:
			self.title = idea_dict['title']
			self.id = idea_dict['id']
	
	
	"""Human-readable string"""
	def __str__(self):
		idea_string = """Idea: (no title)"""
		
		if self.title is not None:
			idea_string = """Idea: """ + str(self.title)

		return idea_string



class Feedback(Resource):
	"""A Prodpad Feedback"""
	linked_ideas = []
	
	"""If launched with no ID, then don't query the API"""
	def __init__(self):
		super(Idea, self).__init__(session,"""feedbacks""")
	
	
	"""Get all feedback for an idea"""
	def __init__(self, feedback_dict, idea, session):
		super(Feedback, self).__init__(session,"""feedbacks""")
		self.linked_ideas.append(idea)
		self.id = feedback_dict['id']
		self.dict = feedback.dict
	
	
	"""Human-readable string"""
	def __str__(self):
		feedback_string = """Feedback: (no ID)"""
		
		if self.id is not None:
			feedback_string = """Feedback: """ + str(self.id)

		return feedback_string
	
	


	