# MTAstatus
Status of MTA trains from widget

Pulls the subway name and status from the widget at the site http://service.mta.info/ServiceStatus/status.html?widget=yes

Things to fix: 
-Request access to MTA API instead of scraping

-Children and descendants weren't working properly. Next_parent not available in the lib. Hacked it and went up parents 1 by 1. This is inefficient. 

-This is for specific lines. Change the code for the line statuses you need. 

-When creating the bot on twitter, you must remove your phone number from your primary account and migrate it to the bot. 

-Variable nomenclature can be made more clear

-Automate this with a chron job before I leave my house for work, and before I leave work for home.  
