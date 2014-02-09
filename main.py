import praw
from time import sleep
from collections import deque
import re
import json

r = praw.Reddit("alotBot by /u/thirdegree")

def _login():
	USERNAME = raw_input("Username?\n> ")
	PASSWORD = raw_input("Password?\n> ")
	r.login(USERNAME, PASSWORD)

Trying = True
while Trying:
	try:
		#_login()
		Trying = False
	except praw.errors.InvalidUserPass:
		print "Invalid Username/password, please try again."

with open("alots") as t:
	alots = json.load(t)

print alots