from flask import Flask
from flask_bootstrap import Bootstrap
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('config')

bootstrap = Bootstrap(app)
db = MongoEngine(app)

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
