import twitter 
#go to apps.twitter.com to get the key and secret info
api = twitter.Api(consumer_key='',
		  consumer_secret='',
		  access_token_key='',
		  access_token_secret='')

from datetime import datetime, date, time
dt = datetime.now()
timeStamp = dt.strftime("%A. %B, %d %Y %I:%M%p")
oneMsg = "1 2 3 Delays"
oneDelayMsg = [oneMsg, timeStamp]
OnedatetimeString = ' '.join(oneDelayMsg)
aceMsg = "A C E Delays"
aceDelayMsg= [aceMsg, timeStamp]
ACEdatetimeString = ' '.join(aceDelayMsg)

#Documentation is wrong. Text, receiver,
def oneTrain_delay():
	api.PostDirectMessage(OnedatetimeString, "1559767622")
def oneTrain_planned():
	api.PostDirectMessage(OnedatetimeString, "1559767622")


def aceTrain_delay():
	api.PostDirectMessage(ACEdatetimeString, "1559767622")	

def aceTrain_planned():
	api.PostDirectMessage(ACEdatetimeString, "1559767622")


def aceTrain_status():
	api.PostUpdate(ACEdatetimeString)

def oneTrain_status():
	api.PostUpdate(OnedatetimeString)
