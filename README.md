# truiSMS

A Flask SMS app that replies to texts with one of Jenny Holzer's "Truisms" (1978-1987). https://www.moma.org/collection/works/63755

## Getting Started

This project uses Python 3.6.2. To use the Twilio webhook during development, you will need to spin up an introspected tunnel to your localhost. I recommend using [ngork](https://ngrok.com/download). _You will need to create a [Twilio](https://www.twilio.com/try-twilio) developer account_ to receive testing credentials and configure a phone number to receive messaging requests from your tunnel's URL route.

### Prerequisites

All dependencies are versioned and maintained in a requirements file. To install project requirements, run:

```
$ pip install -r requirements.txt
```

### Installing

After installing requirements, activate the virtualenv.

```
$ source truisms/bin/activate
```

Configure your tunnel to forward to localhost:5000. To run the development server, run: 

```
$ python app.py
```

When you text the number you associated with your local tunnel, you should see the following output:

```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [09/Nov/2017 10:54:31] "POST /sms HTTP/1.1" 200 -
```

## Running the tests

The unit tests use the nose library. To run the tests:

```
$ nosetests
```

You should see output something like this:

```
..................................
----------------------------------------------------------------------
Ran 34 tests in 1.440s

OK
```

## Deployment

The live version of truiSMS is hosted on Heroku.

## Built With

* [Flask](http://flask.pocoo.org/docs/0.12/) - The web framework used
* [Twilio](https://www.twilio.com/console/sms/getting-started/developer-docs) - Programmable SMS API
* [Heroku](https://devcenter.heroku.com/) - Application build and deployment

## Authors

* **Jenna Feldman** - *Initial work* - [feljen](https://github.com/feljen)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
