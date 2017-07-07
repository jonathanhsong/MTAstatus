import twitter 
api = twitter.Api(consumer_key='',consumer_secret='',access_token_key='',access_token_secret='')

#Documentation is wrong. Text, receiver,
def oneTrain_delay():
	api.PostDirectMessage('1 2 3 Delays', "user_id")

def oneTrain_status():
	api.PostUpdate('1 2 3 Subway Status no longer on time')

def aceTrain_delay():
	api.PostDirectMessage('A C E Delays', "user_id")	

def aceTrain_status():
	api.PostUpdate('A C E Subway Status no longer on time')
