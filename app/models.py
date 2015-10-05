import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class Keyword(db.Document):
    added = db.DateTimeField(default=datetime.datetime.now, required=True)
    keyword = db.StringField(max_length=25, required=True)

class User(db.Document):
    username = db.StringField(max_length=64, required=True)
    role = db.StringField(max_length=64, required=True)
    password_hash = db.StringField(max_length=128)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
