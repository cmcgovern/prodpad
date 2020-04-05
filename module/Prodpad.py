# -*- coding: utf-8 -*-

from module.Resources import Idea

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
	
	def idea(self, id):
		"""docstring for idea"""
		idea = Idea(id, self)
		
		return idea




