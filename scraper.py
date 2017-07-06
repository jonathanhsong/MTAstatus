from bs4 import BeautifulSoup
import requests
import re
#import os only needed if outputing to local drive  
from mtaDM import *

page = requests.get("http://service.mta.info/ServiceStatus/status.html?widget=yes")
page
page.content
if page.status_code == 200:
	print ("MTA Server Online") 
else: 
	print ("Server Error")

css_soup = BeautifulSoup(page.content, 'html.parser')
#This finds the good service trains first
for gService in css_soup.find_all('span', class_='subway_goodservice'): 
	upOne = gService.parent
	upTwo = upOne.parent
	#Using parents ensures that the status and train are aligned
	#BS4 does not allow for next_parent
	for trainName in upTwo.find_all('img', alt=True):
			print(trainName['alt'], gService.text)

#children/descendants returning something weird. Test method later
for dService in css_soup.find_all('span', class_='subway_delays'): 
	DupOne = dService.parent
	DupTwo = DupOne.parent
	for DtrainName in DupTwo.find_all('img', alt=True):
			print(DtrainName['alt'], dService.text)
			
			dList = DtrainNamep['alt']		
			if "A C E Subway" == dList:
				aceTrain_delay()
			else:
				continue
			if "1 2 3 Subway" == dList:
				oneTrain_delay()
			else:
				continue 

for pService in css_soup.find_all('span', class_='subway_plannedwork'): 
	PupOne = pService.parent
	PupTwo = PupOne.parent
	for PtrainName in PupTwo.find_all('img', alt=True):
			print(PtrainName['alt'], pService.text)

			pList = PtrainName['alt']
			if "A C E Subway" == pList:
				aceTrain_delay()
			else:	
				continue
			if "1 2 3 Subway" == pList:
				oneTrain_delay()
			else:
				continue
