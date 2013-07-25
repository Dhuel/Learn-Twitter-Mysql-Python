
#TODO -Complete task 5


import tweetpony
api = tweetpony.API(consumer_key = "mXtSuwi5Nwx0MbgS3IQpA", consumer_secret = "m5Rxk3yxf9TNJ1Xybu4fkgCMfnOYSby0JzQvW3CKU", access_token = "1016496080-wcdc2W9l0GNaLSYScFJ9QQ6gG3TXURMDXw3eMy5", access_token_secret = "LerRfJOXxpmsgZTrDy3qzwHDPqzfv0KBjJhV0ePrE")
user = api.user
def tweetqu():
  text = raw_input("What would you like to tweet sir? ")
  try:
      api.update_status(status = text)
  except tweetpony.APIError as err:
      print "Sir, we seem to have an error. Twitter returned the error #%i and said: %s" % (err.code, err.description)
  else:
      print "Good job sir, your tweet has been posted"

print "Hello sir, Jarvis is at your service. Would you like to post a tweet?"
text0 = raw_input("")
if (text0 =="Yes"):
  tweetqu()
else:
 print "Good day sir"
	
  
