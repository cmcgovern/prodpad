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

"""
{
	"id": 609006,
	"project_id": 3504,
	"account": {
		"id": 12215,
		"slug": "axway-1",
		"name": "Axway"
	},
	"web_url": "https://app.prodpad.com/ideas/3504/canvas",
	"impact": "11",
	"impact_scaled": "100",
	"effort": "11",
	"effort_scaled": "100",
	"created_at": "2019-01-11 12:15:21",
	"updated_at": "2019-11-28 16:43:34",
	"title": "Support for OpenAPI / Swagger 3.0 API-Specifications in API Manager",
	"description": "<p>Allow users to import a OAS3 definition, create a backend API from this and expose via a frontend API</p>",
	"state": "active",
	"creator": {
		"id": 25365,
		"username": "cmcg0vern",
		"display_name": "Colin McGovern"
	},
	"business_case": {
		"problem": "<p>This is the first step in a phased approach to enhancing API Managers OAS3 offer. This step would be to import an OAS3 definition and create a backend API from this definition. The user would be then able to create a frontend API from this. As part of this feature the API would be exposed with the Swagger 2 elements added in  7.7</p>",
		"value": "<p>MVP (Minimum Viable Product) support of OAS3 in API Manager. Users will be able to import an OAS definitions and create an API from it. </p>"
	},
	"functional_spec": "",
	"notes": "",
	"status": {
		"id": "64039",
		"status": "In Development",
		"added": "2019-10-17 13:05:48"
	},
	"owner": {
		"id": 67718,
		"username": "gschoeman",
		"display_name": "Gian Schoeman"
	},
	"author": null,
	"tags": [
		{
			"id": "170947",
			"tag": "OpenAPI 3.0",
			"added": "2019-11-01 15:59:55"
		},
		{
			"id": "215093",
			"tag": "OAS 3.0",
			"added": "2019-10-17 16:07:54"
		}
	],
	"products": [
		{
			"id": "44702",
			"name": "API Management",
			"added": "2019-03-12 11:21:16"
		}
	],
	"personas": [
		{
			"id": "20902",
			"name": "Flow Manager",
			"added": "2019-03-12 10:56:28"
		}
	],
	"external_links": [
		{
			"id": "211260",
			"external_id": null,
			"title": "RDAPI-15773",
			"url": "https://techweb.axway.com/jira/browse/RDAPI-15773",
			"created_at": "2019-04-10 16:40:03"
		}
	],
	"roadmap_cards": [
		{
			"id": "308636",
			"title": "OpenAPI 3.0 Support Phase2 ",
			"description": "<p>A continuation of the OAS3 work completed in 7.7.20200130</p><p>1. More fine grained validation of OAS3 docs on import</p><p>2. Validation of OAS3 Params at runtime in the gateway</p><p>3. Enhancements to the UI to display and edit more OAS3 fields via the API Manager screens</p><p>4. Add Client Credentials to API Manager Frontend UI and OAS3&nbsp;</p>",
			"column": {
				"id": "134016",
				"title": "Backlog",
				"column_number": "3"
			},
			"roadmap": {
				"id": "44851"
			}
		},
		{
			"id": "276598",
			"title": "OpenAPI 3.0 Support ",
			"description": "<p>Add support for the import and Export of OpenAPI 3.0/Swagger definitions in API Manager.&nbsp;</p><p>More information on what will be supported can be found on the <a href=\"https://community.axway.com/s/question/0D52X00008BMPDRSA5/oas3-support-coverage-in-api-managers-78-release\" rel=\"noopener noreferrer\" target=\"_blank\">Community Portals Discussion</a> section</p><p>As part of this change users will now have the option to Backend APIs while its not published if they wish&nbsp;</p>",
			"column": {
				"id": "134014",
				"title": "May Update Candidates",
				"column_number": "1"
			},
			"roadmap": {
				"id": "44851"
			}
		}
	],
	"mockups": [

	],
	"user_stories": [

	],
	"comments": [
		{
			"id": "238695",
			"comment": "<p>this has to be the most requested support to date....14+ CERS looking for it <span><a data-user-id=\"87444\" href=\"/users/87444/about\">Barry Maher</a></span>&nbsp; <span><a data-user-id=\"67718\" href=\"/users/67718/about\">Gian Schoeman</a></span>&nbsp;</p>",
			"created_by": {
				"id": "67684",
				"username": "jowens",
				"display_name": "John Owens"
			},
			"created_at": "2019-02-22 11:22:38",
			"updated_at": "2019-02-22 11:23:06",
			"replies": [

			]
		}
	],
	"votes": {
		"yea": [
			{
				"id": 87814,
				"voter": {
					"id": "70122",
					"username": "cwiechmann",
					"display_name": "Chris Wiechmann"
				},
				"created_at": "2019-01-16 07:44:53"
			},
			{
				"id": 105816,
				"voter": {
					"id": "25365",
					"username": "cmcg0vern",
					"display_name": "Colin McGovern"
				},
				"created_at": "2019-10-17 13:06:16"
			}
		],
		"nay": [

		],
		"maybe": [

		]
	},
	"files": [

	]
}
"""
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
	
	
	"""Human-readable string"""
	def __str__(self):
		feedback_string = """Feedback: (no ID)"""
		
		if self.id is not None:
			feedback_string = """Feedback: """ + str(self.id)

		return feedback_string
	
	


	