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
(1 hour = 3600)    
waitLoopTime = 0

4. run dailyTradingData.py on a 24/7 running device (raspberry pi/private server ect.)