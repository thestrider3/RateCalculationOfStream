#Import the necessary methods from tweepy library
import tweepy
import time
import json
import sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "ENTER YOUR ACCESS TOKEN"
access_token_secret = "ENTER YOUR ACCESS TOKEN SECRET"
consumer_key = "ENTER YOUR API KEY"
consumer_secret = "ENTER YOUR API SECRET"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        #print data
        all_data = json.loads(data)
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]
	#time=datetime.datetime.now()
	print json.dumps({"time":float(time.time()), "status":tweet, "username":username})
	sys.stdout.flush()
	#time.sleep(2)
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth=tweepy.OAuthHandler('LEbqgSpTblFldGI13LXUNYVOA','dc8i1mfLwmTUtk3K5XnnqW0KJvGfnrjYtphreGFingVBjQGeBb')
    auth.set_access_token('137228501-ZnKjgQS9P8mb6Mfa7SnA78lsV90MSvmuVCUpSE83','NKt5owZ7GWZ4UlMWI4yHwKVxXdXRdKD6z4B643TVXIJ6W')
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['JNURow'])
    stream.filter(locations=[75.00,78.00,32.00,35.00])
