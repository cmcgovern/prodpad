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
			if key == 'add_path_to_url':
				url += '/' + value

		response = requests.get(url, headers=self.session.headers, params=params)
		print(response.text)
		if (response.status_code == requests.codes.ok):
			response_dict = json.loads(response.text) 
		
		return response_dict



class Company(Resource):
	"""docstring for Company"""
	def __init__(self, arg):
		super(Company, self).__init__(session, """roadmaps""")
		self.product_lines = product_lines
		


class ProductLine(Resource):
	"""docstring for ProductLine"""
	
	def getProductLineById(self, id, product_lines):
		"""docstring for getProductLineById"""
		for product_line in product_lines:
			if product_line['id'] == id:
				return product_line
		return None
	
	
	def getProductLineByName(self, name, product_lines):
		"""docstring for getProductLineByName"""
		for product_line in product_lines:
			if product_line['name'] == name:
				return product_line
		return None
	
	
	def __init__(self, session, **kwargs):
		super(ProductLine, self).__init__(session, """roadmaps""")
		self.id = None
		self.name = None
		
		for key, value in kwargs.items():
			if key == 'id':
				self.id = value
				product_line_dict = getProductLineByName(self.id, roadmap_dict['product_lines'])
			if key == 'name':
				self.name = value
				product_line_dict = getProductLineByName(self.name, roadmap_dict['product_lines'])
		
		roadmap_dict = self.loadFromAPI()
		


class Roadmap(Resource):
	"""docstring for Roadmap"""
	
	def __init__(self, session, id):
		super(Roadmaps, self).__init__(session, """roadmaps""")
		self.swimlanes = []
		self.id = id
		roadmap_dict = self.loadFromAPI(id=self.id)
	
	def __str__(self):
		roadmap_string = """Roadmap ID: """ + str(self.id) + """, swimlanes: """ + str([str(swimlane) for swimlane in self.swimlanes])
		return roadmap_string
		


class RoadmapCard(Resource):
	"""A roadmap card cannot be queried directly from the API"""
	def __init__(self, card_dict):
		super(RoadmapCard, self).__init__(None, None)
		self.id = card_dict['id']
		self.title = card_dict['title']
		self.ideas = []
	
	def __str__(self):
		card_string = str(self.title) + """ #Ideas: """ + str(len(self.ideas))
		return card_string



class Idea(Resource):	
	"""If launched with no ID, then don't query the API"""
	def __init__(self):
		super(Idea, self).__init__(None, None)
	
	
	def getFeedback(self):
		"""docstring for getAllFeedback"""
		linked_feedback = []
		
		feedback_items_dict = self.loadFromAPI(id=self.id, add_path_to_url="""feedback""")
		for feedback_item in feedback_items_dict:
			linked_feedback.append(Feedback(feedback_item, self, self.session))
		
		return linked_feedback
	
	
	"""If launched with an ID, then query the API for this idea"""
	def __init__(self, session, **kwargs):
		super(Idea, self).__init__(session,"""ideas""")
		for key, value in kwargs.items():
			if key == 'short_id':
				self.short_id = value
				self.options = {'by_project_id': 'true', 'expand': 'true'} # This allows us to use the visible ID to retrieve ideas
			if key == 'id':
				self.id = value
				self.options = {'expand': 'true'}
		
		self.roadmap_cards = []
		
		# Call API and fill in details
		idea_dict = self.loadFromAPI(id=(self.short_id if self.short_id is not None else self.id), params=self.options)
		
		if idea_dict is not None:
			self.title = idea_dict['title']
			self.id = idea_dict['id']
			for roadmap_card in idea_dict['roadmap_cards']:
				self.roadmap_cards.append(RoadmapCard(roadmap_card))
	
	
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
	def __init__(self, feedback_dict, idea, session):
		super(Feedback, self).__init__(session,"""feedbacks""")
		self.linked_ideas.append(idea)
		self.id = feedback_dict['id']
		self.dict = feedback_dict
	
	
	"""Human-readable string"""
	def __str__(self):
		feedback_string = """Feedback: (no ID)"""
		
		if self.id is not None:
			feedback_string = """Feedback: """ + str(self.id)

		return feedback_string
	
	


	