from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config')

bootstrap = Bootstrap(app)

from app.main import views
from app.main import errors
from app.main import forms
