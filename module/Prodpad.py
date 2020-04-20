# -*- coding: utf-8 -*-

from module.Resources import Idea
from module.Resources import Roadmaps
from module.Resources import ProductLines

class Prodpad(object):
	"""
	This is the starting point. This is where we set up everything needed for API interaction
	"""
	base_url = """https://api.prodpad.com/v1/"""
	headers = {}
	
	def __init__(self, key):
		super(Prodpad, self).__init__()
		self.key = key
		self.headers = {"""Authorization""": """Bearer """ + key}

	
	def idea(self, **kwargs):
		"""docstring for idea"""
		for key, value in kwargs.items():
			if key == 'short_id':
				idea = Idea(self, short_id=value)
			if key == 'id':
				idea= Idea(self, id=value)
		return idea


	def roadmaps(self, **kwargs):
		"""docstring for allroadmaps"""
		roadmaps = None
		my_id = None
		for key, value in kwargs.items():
			if key == 'id':
				my_id = value
				roadmaps = Roadmaps(self, id=my_id)
		
		if my_id is None:
			roadmaps = Roadmaps(self)
		return roadmaps

	
	def product_lines(self, **kwargs):
		"""docstring for product_lines"""
		# Whatever happens, we return a list
		product_lines = []
		
		my_id = None
		for key, value in kwargs.items():
			if key == 'id':
				my_id = value
				product_lines.append(ProductLines(self, id=my_id))
			if key == 'name':
				my_name = value
				product_lines.append(ProductLines(self, name=my_name))
		
		if my_id is None and my_name is None:
			product_lines = ProductLines(self)
		return product_lines



