# MTAstatus
Status of MTA trains from widget

Pulls the subway name and status from the widget at the site http://service.mta.info/ServiceStatus/status.html?widget=yes

Main Issues: Children and descendants weren't working properly. Next_parent not available in the lib. Hacked it and went up parents 1 by 1. This is inefficient. 

Things to improve: Automate this with Twilio to text me when specific trains change from Good to any other state. 
