#This code snippted was taken from the Class Lecture taught by Professor Mike Dewar. In this file, the data obtained from 
#delta.py is parsed using JSON and the time and the difference delta is stored into Redis. The time is made the key as it 
#is unique and delta is attached to it as its value. A key expiration rate of 120 s is set in the method conn.setex() 
#which is sufficient for our purpose.
import json
import sys
import redis

conn = redis.Redis()

while 1:
    line = sys.stdin.readline()
    d = json.loads(line)
    delta = d["delta"]
    time = d["time"]
    status=d["status"]
    username=d["username"]
    rate=d["rate"]
    conn.setex(time, rate, 120)
    print json.dumps({"time":time, "rate": rate, "delta":delta, "status":status, "username":username})
