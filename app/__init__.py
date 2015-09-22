from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app.main import views
from app.main import errors
from app.main import forms
