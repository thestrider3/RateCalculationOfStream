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
    conn.setex(time, delta, 120)
    print json.dumps({"time":time, "delta":delta, "status":status, "username":username})
