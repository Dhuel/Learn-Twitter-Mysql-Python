
#Removed old code
import json
import pprint 
import tweetpony

#We are just learning now. But tell me why its not a good idea to put credentials in Source Code Repositories when we chat
# Because people can copy it and mess with the wrk we do?
api = tweetpony.API(consumer_key = "mXtSuwi5Nwx0MbgS3IQpA", consumer_secret = "m5Rxk3yxf9TNJ1Xybu4fkgCMfnOYSby0JzQvW3CKU", access_token = "1016496080-wcdc2W9l0GNaLSYScFJ9QQ6gG3TXURMDXw3eMy5", access_token_secret = "LerRfJOXxpmsgZTrDy3qzwHDPqzfv0KBjJhV0ePrE")

#+1 for refactoring the tweetqu and removing  the raw_input from the method. Also get into the habit of writing comments in your code

def tweetqu(text):
    """
Method used to post tweets
    """
    try:
      api.update_status(status = text)
    except tweetpony.APIError as err:
      print "Sir, we seem to have an error. Twitter returned the error #%i and said: %s" % (err.code, err.description)
    else:
      print "Good job sir, your tweet has been posted, %s" %(text)


def printposts():
    """
    Prints the tweets from the users timeline
    """
    my_stuff = api.user_timeline()
    l = 0 
    for each_entry in (my_stuff):
        pprint.pprint(my_stuff[l]['text'])
        l = l+1

#TODO refactor this method
def get_tweets(text2):
 search = api.search_tweets(q = text2)
 l = 0
 for each_entry in (search):
  print "*******************************"
  pprint.pprint(search[l]['text'])
  print "*******************************"
  l = l+1


def main():
 #TODO figure out how to use python main()
 #So basically what i understand is that the main allows the code to be imported without causing bad side effects. Apparently it automatically runs even if its imported as a module 
 text0 = raw_input("\nHello sir, Jarvis is at your service. Would you like to post a tweet?\n")
 if(text0 =="Yes"):
  tweetqu(raw_input("What would you like to tweet?\n"))
 else:
  text1 = raw_input("Would you like to see your posts?\n")
  if (text1 == "Yes"):
   printposts()
  else:
   text3 = raw_input("Would you like to searh for specific tweets?\n")
   if (text3 == 'Yes'):
    get_tweets(raw_input("What would you like to receive tweets about?\n"))
   else:
     print "Good day sir \n"
if __name__ == "__main__":
 main()



'''
#used to print users screen name
print str( api.user.screen_name)+ " is the username."
'''
'''
#code segment to get status of a follower, only works if follower has posted on wall - potentially useful to check each status for keywords(flaw: only works on followers)
my_followers = api.user.followers()
pprint.pprint (my_followers[1]['status']['text'])
'''
'''
#Prints post based on the id number of the post
get_idnum  = api.user_timeline()
pprint.pprint( get_idnum[0]['id'])
id_num = (get_idnum[0]['id'])
my_tweet = api.get_status(id =id_num)
pprint.pprint (my_tweet['text'])
'''
'''
#gets texts form friends that you follow - useable for finding posts on relevant topics
f_ids = api.friends_ids()
pprint.pprint (f_ids)
tweets = [api.user_timeline(user_id = id) for id in f_ids]
pprint.pprint(tweets[0][0]['text'])
'''


'''
potentially useful code
friend_tl = api.user_timeline(user_id = friendsids)
pprint.pprint(friend_tl[0])

converted_json_to_dictionary = json.loads(my_tweet['json'])
pprint.pprint(converted_json_to_dictionary['users'])
'''
