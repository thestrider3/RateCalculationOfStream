#I have used Tweepy Library as it provides easy methods to connect with Twitter Streaming API
#I have imported Time Library to easily get current system time
#The code snippets used here were taken from this blog: http://adilmoujahid.com/posts/2014/07/twitter-analytics/
#Import the necessary methods from tweepy library
import tweepy
import time
import json
import sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 



#This is a basic listener that which received the streaming data. The data is further converted to JSON format for easy 
#parsing and then the tweet text, user name is parsed out from the data.
class StdOutListener(StreamListener):

    def on_data(self, data):
        #print data
        all_data = json.loads(data)
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]
	#time=datetime.datetime.now()
	#current system time is recorded using the time.time() and is printed to stdout
	print json.dumps({"time":float(time.time()), "status":tweet, "username":username})
	sys.stdout.flush()
	#time.sleep(2)
        return True
        #if an error occurs in the data stream, the error status is printed for easy debugging
    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    #there is a Listner which listens to the events occuring on the stream
    l = StdOutListener()
    #Consumer API keys and access tokens are needed by twitter for authentication
    auth=tweepy.OAuthHandler("ENTER YOUR API KEY","ENTER YOUR API SECRET")
    auth.set_access_token("ENTER YOUR ACCESS TOKEN","ENTER YOUR ACCESS TOKEN SECRET")
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: Here I have chosen 'JNURow' as my keyword. I have 
    #chosen this particular keyword, as this was the hashtag which was trending when the row occured.
    stream.filter(track=['JNURow'])
    #these are the latitudes and longitudes of Jammu and Kashmir; only tweets containing belonging to these range of latitudes
    #and longitudes have been taken into consideration.
    stream.filter(locations=[75.00,78.00,32.00,35.00])
