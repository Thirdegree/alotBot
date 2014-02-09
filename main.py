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

def alot_types(body):
	types = {"care":False, "fire":False, "mist":False, "straw":False,"beer cans":False,
			"charging":False, "hear":False, "like":False, "dangerous":False}
	for i in types:
		if 