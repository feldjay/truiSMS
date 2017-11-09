import csv
import random
from flask import Flask
from twilio import twiml


app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    with open('truisms.csv', 'r') as f:
        reader = csv.reader(f)
        truisms = list(reader)

    truism = str(random.choice(truisms))

    resp = twiml.Response()
    resp.message(truism)
    return str(resp)


if __name__ == '__main__':
    app.run()
