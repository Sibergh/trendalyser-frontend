import datetime
from flask import url_for
from app import db

class Keyword(db.Document):
    added = db.DateTimeField(default=datetime.datetime.now, required=True)
    keyword = db.StringField(max_length=25, required=True)
