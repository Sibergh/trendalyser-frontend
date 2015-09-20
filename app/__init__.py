from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)

Bootstrap(app)

from app.main import views
from app.main import errors
