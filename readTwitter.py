
#TODO -Complete task 5
import json
import pprint 
import tweetpony
api = tweetpony.API(consumer_key = "mXtSuwi5Nwx0MbgS3IQpA", consumer_secret = "m5Rxk3yxf9TNJ1Xybu4fkgCMfnOYSby0JzQvW3CKU", access_token = "1016496080-wcdc2W9l0GNaLSYScFJ9QQ6gG3TXURMDXw3eMy5", access_token_secret = "LerRfJOXxpmsgZTrDy3qzwHDPqzfv0KBjJhV0ePrE")
def tweetqu():
  text = raw_input("What would you like to tweet sir? ")
  try:
      api.update_status(status = text)
  except tweetpony.APIError as err:
      print "Sir, we seem to have an error. Twitter returned the error #%i and said: %s" % (err.code, err.description)
  else:
      print "Good job sir, your tweet has been posted"

print "\nHello sir, Jarvis is at your service. Would you like to post a tweet?"
text0 = raw_input("")
if (text0 =="Yes"):
  tweetqu()
else:
 print "Good day sir \n"

print str( api.user.screen_name)+ " is the username."
stu = "Hello"
'''
*********************************************************************
nes=xt project is to use this key to find post
360528573196550145
*********************************************************************
'''
my_stuff = api.user_timeline()
l = 0
for each_entry in (my_stuff):
   pprint.pprint(my_stuff[l]['text'])
   l = l +1
'''
my_tweet = api.user.followers()
#my_tweet = api.get_status(id =1)
#print "The tweet is %s" %(my_tweet)
converted_json_to_dictionary = json.loads(my_tweet['json'])
pprint.pprint(converted_json_to_dictionary['users'])
'''
