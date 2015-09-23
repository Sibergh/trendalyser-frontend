from flask import Flask
from flask_bootstrap import Bootstrap
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config.from_object('config')

app.debug = True #Change this to false to remove debug toolbar for release version

bootstrap = Bootstrap(app)
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)
toolbar = DebugToolbarExtension(app)

from app.main import views
from app.main import errors
from app.main import forms
