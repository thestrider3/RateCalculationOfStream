
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

    print json.dumps({"rate":rate})
    sys.stdout.flush()

    time.sleep(0.5)
    auth=tweepy.OAuthHandler('LEbqgSpTblFldGI13LXUNYVOA','dc8i1mfLwmTUtk3K5XnnqW0KJvGfnrjYtphreGFingVBjQGeBb')
    auth.set_access_token('137228501-ZnKjgQS9P8mb6Mfa7SnA78lsV90MSvmuVCUpSE83','NKt5owZ7GWZ4UlMWI4yHwKVxXdXRdKD6z4B643TVXIJ6W')
    api = tweepy.API(auth)
    print api.me().name
    count=count+1
    tweet = "The rate of "+str(count)+"is "+str(rate)
    status = api.update_status(status=tweet)
    
