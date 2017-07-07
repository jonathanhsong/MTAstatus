import twitter 
#go to apps.twitter.com to get the key and secret info
api = twitter.Api(consumer_key='',
		  consumer_secret='',
		  access_token_key='',
		  access_token_secret='')
from datetime import datetime, date, time
'''
Working on inputing a timestamp 
dt = datetime.now()
timeStamp = dt.strftime("%A. %B, %d %Y %I:%M%p")
oneMsg = "1 2 3 Delays"
oneDelayMsg = [timeStamp, oneMsg]
print(oneDelayMsg)

'''


#Documentation is wrong. Text, receiver,
def oneTrain_delay():
	api.PostDirectMessage('1 2 3 Delays', "user_id")

def oneTrain_planned():
	api.PostDirectMessage('1 2 3 Planned work', "user_id")


def aceTrain_delay():
	api.PostDirectMessage('A C E Delays', "user_id")	

def aceTrain_planned():
	api.PostDirectMessage('A C E Planned work', "user_id")


#Twitter prevents posting multiple status. Maybe I can return a date.
def aceTrain_status():
	api.PostUpdate('A C E Subway Status no longer on time')

def oneTrain_status():
	api.PostUpdate('1 2 3 Subway Status no longer on time')
