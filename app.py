import csv
import random
from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client


app = Flask(__name__)
app.config.from_envvar('APP_CONFIG')

client = Client(app.config['TWILIO_ACCOUNT_SID'], app.config['TWILIO_AUTH_TOKEN'])


@app.route('/sms', methods=['POST'])
def sms():
    with open('truisms.csv', 'r') as f:
        reader = csv.reader(f)
        truisms = list(reader)

    truism = random.choice(truisms)[0]

    resp = MessagingResponse()
    resp.message(truism)
    return str(resp)


if __name__ == '__main__':
    app.run()
