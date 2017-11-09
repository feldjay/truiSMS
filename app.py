import csv
import random
from config import *
from flask import Flask
from twilio.twiml.messaging_response import Message, MessagingResponse
from twilio.rest import Client


client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    with open('truisms.csv', 'r') as f:
        reader = csv.reader(f)
        truisms = []
        for row in reader:
            truisms.append(row)

    truism = str(random.choice(truisms)).strip("[']")

    resp = MessagingResponse()
    resp.message(truism)
    return str(resp)


if __name__ == '__main__':
    app.run()
