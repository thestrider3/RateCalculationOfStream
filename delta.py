#the code snippet used here was taken from the Class Lecture held by Professor Mike Dewar
import json
import sys
lastArrival=0
while True:
	line=sys.stdin.readline()
	d=json.loads(line)
	#extracting time, status and username from the JSON data received from twitter_getdata.py
	t=d["time"]
	status=d["status"]
        username=d["username"]
        #ignoring the first message as there is no message before it to calculate the time difference
	if lastArrival==0:
		lastArrival=t
		continue
	delta=t-lastArrival
	lastArrival=t
	#calculating rate of arrival between two tweets
	print json.dumps({"delta": delta, "time": t, "status":status, "username":username})
	sys.stdout.flush()
