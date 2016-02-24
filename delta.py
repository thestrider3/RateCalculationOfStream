import json
import sys
lastArrival=0
while True:
	line=sys.stdin.readline()
	d=json.loads(line)
	t=d["time"]
	status=d["status"]
        username=d["username"]
	if lastArrival==0:
		lastArrival=t
		continue
	delta=t-lastArrival
	lastArrival=t
	print json.dumps({"delta": delta, "time": t, "status":status, "username":username})
	sys.stdout.flush()
