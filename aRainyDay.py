import urllib.request
import json
from twilio.rest import Client
import schedule
import time



#accoutn details from Twilio
account_sid = 'AC42f185b617ac78871daab6afdffdbbf2'
auth_token = '8897f275af08676e0c0fa67640088473'
client = Client(account_sid, auth_token)

#opening url where data is coming from 
url = 'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/331087?apikey=qTzkDN1V7WsRrk72gcyf3zEaOz2UkQG0'
source = urllib.request.urlopen(url)

#reads JSON file to a python object
data = json.load(source)

def smsTXT(precipCheck):
    if precipCheck == True:
        message = client.messages.create(
                                      body='BRING A COAT!',
                                      from_='+19014727942',
                                      ##where your phone number goes
				      to=' '
                                  )
        print(message.sid)

def precipProb(data):
    hour = 0
    precipCheck = False

    while hour < (len(data)):
        precipVal = data[hour]['PrecipitationProbability']
        print(precipVal)

        if(precipVal) > 15:
            precipCheck = True
        hour += 1

    smsTXT(precipCheck)


def main():
    schedule.every().day.at("07:30").do(precipProb, data)
    while True:
        schedule.run_pending()
        time.sleep(60)

main()
