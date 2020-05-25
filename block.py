#!/usr/local/bin/python
import json
import praw

###############################################################################

# enter bot id here
bot_id = ''

# enter bot secret here
bot_secret = ''

# enter reddit username
username = ''

# enter reddit password
password = ''

# leave this as "bot"
script_agent = 'bot'

###############################################################################

# read accounts into list
with open('blocklist.txt', 'r') as file:
    accounts = file.read().split('\n')
    accounts = list(filter(lambda x: len(x) > 0, accounts))

# access reddit programmatically
reddit = praw.Reddit(client_id=bot_id,
                    client_secret=bot_secret,
                    user_agent=script_agent,
                    username=username,
                    password=password)

blocked = 0

# block each user one by one
for user in accounts:
    try:
        reddit.redditor(user).block()
        print("blocked user " + user)
        blocked += 1
    except Exception as e:
        print(str(e))

print("successfully blocked " + str(blocked) + " accounts")
