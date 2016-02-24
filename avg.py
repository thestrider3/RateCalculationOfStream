
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
    if not keys:
    	keys=[]

    values = conn.mget(keys)

    try:
        deltas = [float(v) for v in values]
    except TypeError:
        print keys
        continue

    if len(deltas):
        rate = sum(deltas)/float(len(deltas))
    else:
        rate = 0
    auth=tweepy.OAuthHandler("ENTER YOUR API KEY","ENTER YOUR API SECRET")
    auth.set_access_token("ENTER YOUR ACCESS TOKEN" ,"ENTER YOUR SECRET ACCESS TOKEN")
    api = tweepy.API(auth)
    print api.me().name
    count=count+1
    tweet = "The rate of "+str(count)+"is "+str(rate)
    status = api.update_status(status=tweet)
    
