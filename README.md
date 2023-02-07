# Developed by Kuro
## https://snipfeed.co/imkuro
### Questions or concerns dm me on insta or discord



## Setup

1. make a twilio account (free trail for a few months)
* https://twilio.com

2. install all needed requirements

~$ pip install requirements.txt

3. setup the config file with api keys and phone numbers

- go to creds.py and edit it
### Your Account SID from twilio.com/console
account_sid = ""
### Your Auth Token from twilio.com/console
auth_token  = ""
### the phone number you want to send the updates to
phoneNumber = ""
### twilio phone number 
phonefrom = ""
### how many seconds to wait till it starts looping
- if you start this at 9 PM and want it to send a message at 7 AM you would enter 36000 becuase thats 10 hours.

(1 hour = 3600)    
waitLoopTime = 0

4. change the choices.json file to the stocks/options/futures ect. you want. 
- use https://tvdb.brianthe.dev/ to get the correct info


5. run dailyTradingData.py on a 24/7 running device (raspberry pi/private server ect.)
