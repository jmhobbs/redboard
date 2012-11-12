`redboard` is a simple dashboard for Redis.

It's main feature is the fact that you can embed it in other Flask applications through the power of Blueprints.

Thanks to `rq-dashboard` for inspiring me to learn how to make that work.

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

This will create redboard based on the URL `/edboard` in your Flask app.

