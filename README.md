`redboard` is a simple dashboard for Redis.

It's main feature is the fact that you can embed it in other Flask applications through the power of Blueprints.

Thanks to `rq-dashboard` for inspiring me to learn how to make that work.

Thanks to `RedisLive` for some inspiration on what a Redis dashboard should be.

## Installing

```console
$ git clone https://github.com/jmhobbs/redboard.git
$ python setup.py install
```

## Running

```console
$ redboard_server.py
* Running on http://127.0.0.1:5000/
...
```

### Monitor

For the graphs to work, you also need to run the monitor.  This queries Redis on a one second interval and stores the data for redboard to interpret.

```console
$ redboard_monitor.py
* Running on http://127.0.0.1:5000/
...
```


## Embedding into your Flask app

```python
from flask import Flask
from redboard import RedBoard


app = Flask(__name__)
RedBoard(app)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
```

This will create redboard based on the URL `/redboard` in your Flask app.

