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
	return USERNAME

Trying = True
while Trying:
	try:
		USERNAME = _login()
		Trying = False
	except praw.errors.InvalidUserPass:
		print "Invalid Username/password, please try again."

with open("alots") as t:
	alots = json.load(t)

done = deque(maxlen=200)

def alot_types(body):
	types = {"care":False, "fire":False, "mist":False, "straw":False,"beer cans":False,
			"charging":False, "hear":False, "like":False, "dangerous":False}
	for i in types:
		if i in body:
			types[i]=True
	if any([types[i] for i in types]):
		return([i for i in types if types[i]])
	else:
		return ["default"]

def find_alots(body):
	pattern = "(\w+ ){0,4}alot,* (\w+[ ]{0,1}){0,5}"
	t = re.search(pattern, body)
	if t:
		return alot_types(t.group())
	return ""

def main():
	comments = r.get_comments("thirdegree")
	for post in comments:
		print post.author.name.lower()
		if post.id not in done and post.author.name.lower() != USERNAME.lower():
			done.append(post.id)	
			postsAlots = find_alots(post.body)
			print "here"
			if postsAlots:
				rep = "\n\n".join(alots[i] for i in postsAlots)
				post.reply(rep+u"\n\n-------------\n\n^^[All\u00A0pictures\u00A0from\u00A0Hyperbole\u00A0and\u00A0a\u00A0half](http://hyperboleandahalf.blogspot.com/2010/04/alot-is-better-than-you-at-everything.html)")
				sleep(2)

running = True
while running:
	try:	
		print USERNAME
		main()
		sleep(10)
	except praw.errors.RateLimitExceeded:
		print "Rate limit exceeded, sleeping 1 min"
