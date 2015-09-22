#!env/bin/python
from app import app
from flask.ext.script import Manager
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap(app)
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
