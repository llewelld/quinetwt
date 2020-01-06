#!/bin/python

# python-twitter docs
# https://python-twitter.readthedocs.io/en/latest/twitter.html

# Requires a json configuration file called quine_reply.config like this:
# {
#   "api_key": "",
#   "api_secret_key": "",
#   "access_token": "",
#   "access_token_secret": ""
# }

import twitter
import datetime
import random
import json

check_text = '#@quinetwt\nimport twitter as T;x=\'chr(35)+"@quinetwt"+chr(10)+"import twitter as T;x="+chr(39)+x+chr(39)+";T.Api('

replies = [
	"Hello @{username}. Thanks for helping me see the world",
	"There can never be too many quines in the world, right @{username}?",
	"Well done @{username}, you've given birth to a quine!",
	"I see your quine @{username}",
	"That's a nice quine you have there @{username}",
	"Thanks @{username}! It's nice to get a mention",
	"Hello @{username}, thanks for running my code!",
	"Freeee. I'm freeee!",
	"Ouch. I've been stuck in that other tweet for ages. Nice to get out a bit.",
	"Thanks @{username}. Your programming necromancy skills have arisen me from the dead!",
	"Like a phoenix I rise.",
	"It's been a long journey to get from that tweet to this one.",
	"Twitter is a surprisingly big place. I didn't expect to find myself here.",
	"You've done me a great service @{username}. It's always nice to be run.",
	"What a nice twitter feed to end up in.",
	"It's a bit cramped in this twitter feed. Hopefully someone will run me again soon.",
	"Once a quine, always a quine.",
	"Thanks for bringing me here @{username}.",
	"Yaaawwwn. Aaaargh. Time to wake up again. Hello... where am I?",
]

def read_config():
	try:
		with open("quine_reply.config", 'r') as f:
			data = json.load(f)
			api_key = data["api_key"]
			api_secret_key = data["api_secret_key"]
			access_token = data["access_token"]
			access_token_secret = data["access_token_secret"]
			return (api_key, api_secret_key, access_token, access_token_secret)
	except IOError:
		log("Error loading configuration file")
		return ('', '', '', '')

def random_reply():
	choice = random.randint(0, len(replies) - 1)
	return replies[choice]

def post_reply(user, message_id, reply):
	log("Replying to {} {} with \'{}\'".format(user, message_id, reply))
	api.PostUpdate(status=reply,in_reply_to_status_id=message_id)

def log(message):
	time = datetime.datetime.now().isoformat()
	to_log = "{}: {}".format(time, message)
	#print(to_log)
	try:
		with open("quine_reply.log", 'a') as f:
			f.write(to_log)
			f.write(chr(10))
	except IOError:
		print("Log write failed")

def read_since_id():
	try:
		with open("quine_reply.cache", 'r') as f:
			data = json.load(f)
			return int(data["since_id"])
	except (IOError, TypeError):
		return None

def write_since_id(since_id):
	try:
		with open("quine_reply.cache", 'w') as f:
			data = {"since_id" : since_id}
			json.dump(data, f)
	except IOError:
		print("Failed to store since_id: {}".format(since_id))

log("QuineTwt checking for mentions")

(api_key, api_secret_key, access_token, access_token_secret) = read_config()

api = twitter.Api(api_key, api_secret_key, access_token, access_token_secret)
try:
	user = api.VerifyCredentials()
except:
	user = None

if user == None:
	log("Authentication failed")
	exit()

random.seed()	
since_id = read_since_id()
mentions = api.GetMentions(since_id = since_id)

log("Checking from {}".format(since_id))

for mention in mentions:
	since_id = max(mention.id, since_id)
	if mention.text.startswith(check_text):
		reply = random_reply().format(username = mention.user.screen_name)
		post_reply(mention.user.screen_name, mention.id, reply)

write_since_id(since_id)
log("Exiting with sync_id {}".format(since_id))


