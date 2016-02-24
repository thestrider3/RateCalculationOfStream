#The average rate calculation in this file is done by the code snippet demonstrated by Professor Mike Dewar in the Class Lecture.
#Tweepy Library is imported as it provided easy methods for authentication as well as posting tweets programmatically
import redis
import json
import time
import sys
import tweepy
from tweepy import OAuthHandler
conn = redis.Redis()
count=0

while 1:

    pipe = conn.pipeline()

    keys = conn.keys()
    #I have added this line as sometimes keys expire in Redis before they could be accessed and hence lead to a null value
    #Now if this value is again to find out deltas, then they give a TypeError exception
    if not keys:
    	keys=[]

    values = conn.mget(keys)

    try:
        deltas = [float(v) for v in values]
    except TypeError:
        print keys
        continue
#Here a moving average is created by taking the sum of the deltas and diving by length. The deltas keep on increasing as
#data arrives in twitter_getdata.py and due to the use of pipes.
    if len(deltas):
        rate = sum(deltas)/float(len(deltas))
    else:
        rate = 0
    auth=tweepy.OAuthHandler("ENTER YOUR API KEY","ENTER YOUR API SECRET")
    auth.set_access_token("ENTER YOUR ACCESS TOKEN" ,"ENTER YOUR SECRET ACCESS TOKEN")
    api = tweepy.API(auth)
    print api.me().name
    #I have added a count variable as Twitter doesn't allow to print duplicate rates which may occur if tweets arrive at the same time
    count=count+1
    tweet = str(count)+" rate : "+str(rate)
    status = api.update_status(status=tweet)
    
