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
	upTwo = gService.parent.parent
	#Using parents ensures that the status and train are aligned
	#BS4 does not allow for next_parent
	for trainName in upTwo.find_all('img', alt=True):
			print(trainName['alt'], gService.text)

#children/descendants returning something weird. Test method later
for dService in css_soup.find_all('span', class_='subway_delays'): 
	DupTwo = dService.parent.parent
	for DtrainName in DupTwo.find_all('img', alt=True):
			print(DtrainName['alt'], dService.text)
			
			dList = DtrainName['alt']		
			if "A C E Subway" == dList:
				aceTrain_status()
				aceTrain_delay()
			elif "7 Subway" == dList:
				#oneTrain_delay(dList['alt']);
				oneTrain_status()
			else:
				continue 

for pService in css_soup.find_all('span', class_='subway_plannedwork'): 
	PupTwo = pService.parent.parent
	for PtrainName in PupTwo.find_all('img', alt=True):
			print(PtrainName['alt'], pService.text)

			pList = PtrainName['alt']
			if "1 2 3 Subway" == pList:
				oneTrain_planned()
				oneTrain_status()
			elif "A C E Subway" == pList:
				aceTrain_planned()
				aceTrain_status()
				break 
