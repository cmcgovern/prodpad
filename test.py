#!/usr/bin/python3

from prodpad import Prodpad

key="""b4700256516b6e3ea2ed3aadd995e32b7fa156a73f7326aa0fe93cdee9c3e678"""

test = Prodpad(key)

idea = test.idea('729942')

print(idea)
