
#Removed old code
import csv
import sys
import json
import pprint 
import tweetpony
import MySQLdb

#Dev twitter information
api = tweetpony.API(consumer_key = "mXtSuwi5Nwx0MbgS3IQpA", consumer_secret = "m5Rxk3yxf9TNJ1Xybu4fkgCMfnOYSby0JzQvW3CKU", access_token = "1016496080-wcdc2W9l0GNaLSYScFJ9QQ6gG3TXURMDXw3eMy5", access_token_secret = "LerRfJOXxpmsgZTrDy3qzwHDPqzfv0KBjJhV0ePrE")

def tweetqu(text):
    """Method used to post tweets"""
    try:
      api.update_status(status = text)
    except tweetpony.APIError as err:
      print "Sir, we seem to have an error. Twitter returned the error #%i and said: %s" % (err.code, err.description)
    else:
      print "Good job sir, your tweet has been posted, %s" %(text)


def writeT():
    """
   Writes to text file 
    """
    db=MySQLdb.connect(host='localhost', user= 'root', passwd='cldc@dm!n')
    cursor = db.cursor()
    cursor.execute('USE CLDC')
    my_stuff = api.user_timeline()
    l = 0
    tweets =open('tweets.txt','w') #clear text file
    tweets.close() 
    for each_entry in (my_stuff):
	dhuel = (my_stuff[l]['text'])
	tweets = open("tweets.txt",'a')
	tweets.write(dhuel+'\n')
	tweets.close()
        l = l+1
def printposts():
 my_stuff = api.user_timeline()
 l = 0
 for each_entry in (my_stuff):
   pprint.pprint(my_stuff[l]['text'])
   l = l+1
 
def get_tweets(text2):
 search = api.search_tweets(q = text2)
 l = 0
 for each_entry in (search):
  print "*******************************"
  pprint.pprint(search[l]['text'])
  print "*******************************"
  l = l+1

#TODO Take text file and save it in the MYsql database
#MYSQL database
def editMySQL():
 writeT()
 mydb =MySQLdb.connect(host='localhost', user='root',passwd='cldc@dm!n',db='CLDC')
 cursor =mydb.cursor()
 cursor.execute("TRUNCATE tweets")
 csv_data = csv.reader(file('tweets.txt'))
 for row in csv_data:
    tweet =row[0]
    cursor.execute("INSERT INTO tweets VALUES (%r)" %tweet)
 mydb.commit()
 cursor.close()
 print "Tweets have been added to database"

def main():
 text0 = raw_input("\nHello sir, Jarvis is at your service. What would you like to do? \n1. Write a new tweet \n2. See your posts \n3. Search for specific tweet\n4. Write your tweets to a text file\n5. Save tweets in MySQL database\n6. Quit\n")
 if(text0 =="1"):
  tweetqu(raw_input("What would you like to tweet?\n"))
 elif(text0 =="2"):
  printposts()
 elif (text0 =="3"):
  get_tweets(raw_input("What would you like to receive tweets about?\n"))
 elif (text0 =="4"):
  writeT()
  print "Tweets have been written to tweets.txt"
 elif (text0 =="5"):
  editMySQL()
 else:
  sys.exit()  
 print "Task complete!\n"
 main()
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
