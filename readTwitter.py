
#TODO -Complete task 1 here
#More stuff here 
# Pretty sure i understand how to use modules but now i'm on the instillation part of it using pip

# i chose an api to use called tweet pony and i think i installed it correctly but im having probs applying it. I'm trying to get the usag example to work then understand more from there

import tweetpony
api = tweetpony.API(consumer_key = "abc", consumer_secret = "def", access_token = "ghi", access_token_secret = "jkl")
user = api.user
print "Hello, @%s!" % user.screen_name
text = raw_input("What would you like to tweet? ")
try:
    api.update_status(status = text)
except tweetpony.APIError as err:
    print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
else:
    print "Yay! Your tweet has been sent!"
  
