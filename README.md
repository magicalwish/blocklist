# What does this do?
This allows you to block a list of reddit accounts found in `blocklist.txt`. Enter each account on its own line. The two accounts listed in the file currently are just examples of how to format the file.

# How to run this file?

Go to your [app preferences](https://www.reddit.com/prefs/apps). Click the "Create app" or "Create another app" button. Fill out the form like so:
 - name: whatever
 - App type: script
 - description: leave blank
 - about url: leave blank
 - redirect url: https://reddit.com/
 
Hit the "create app" button. Make note of the client ID and client secret. They should look something like:
 - client ID: p-jcoLKBynTLew
 - client secret: gko_LXELoV07ZBNUXrvWZfzE3aI
 
You now have the 4 values you need to fill out the configuration at the top of `block.py`. Add those values like so: 

```python

# enter bot id here
bot_id = 'p-jcoLKBynTLew'

# enter bot secret here
bot_secret = 'gko_LXELoV07ZBNUXrvWZfzE3aI'

# enter reddit username
username = 'coolredditusername123'

# enter reddit password
password = 'coolredditpassword123'

# leave this as "bot"
script_agent = 'bot'
```

Now run the python file using python3: `$(which python3) block.py`. If successful you should see a message like `successfully blocked 99 accounts`.
