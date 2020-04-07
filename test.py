#!/usr/bin/python3

from prodpad import Prodpad

key="""b4700256516b6e3ea2ed3aadd995e32b7fa156a73f7326aa0fe93cdee9c3e678"""

test = Prodpad(key)

print("Getting idea")
print("############")
idea = test.idea('3504')
print(idea)
print("############\n\n")
print("Getting feedback")
print("############")
feedback_items = idea.getFeedback()

for feedback in feedback_items:
	print(feedback)
print("############\n\n")
