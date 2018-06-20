logsworth
---

A simple API to create and serve logs.

Usage:

```sh
$ pip install -r requirements.txt
$ python app.py
```

Send some restful commands:

####POST
```sh
$ curl "http://localhost:5000/api/v1/logs.json" -u logsworth:welldonesir -i -d '2016-02-11T23:05:03.803616+00:00 heroku[router]: at=info method=POST path="/v1/posts" host=api.example.comrequest_id=12345 dyno=web.1 connect=0ms service=100ms status=200 bytes=358' -X POST -H "Content-Type: text/plain"
```

####GET
```
$ curl "http://localhost:5000/api/v1/logs.json?start_time=2010-11-10T23:05:03.803616+00:00&end_time=2017-11-10T23:05:03.803616+00:00" -u logsworth:welldonesir -i
```

Or with your own testing methods. There is some basic auth (thanks to
Flask-HTTPAuth) User is `logsworth` password is `welldonesir` flask defaults to
localhost on port 5000, as you can see from the above curl commands.

Other notes:

I used flask because it's quick to make RESTFUL APIs with. I also used sqlite
because it's fairly easy to get setup as well. I'd rather munge files than set
up a DB when making a 1 hour project.

For the future, rate limiting would be a good idea. If this was for more than
one host, I would probably have a column for that as well. That's it. Enjoy!
