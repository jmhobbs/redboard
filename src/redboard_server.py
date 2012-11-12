import os
from flask import Flask
from redboard import RedBoard

app = Flask(__name__)

if os.getenv('REDBOARD_SETTINGS'):
    app.config.from_envvar('REDBOARD_SETTINGS')

RedBoard(app, '')
app.run()
