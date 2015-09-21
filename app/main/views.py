from flask import render_template, redirect, url_for
from app import app
from .forms import addKeywordForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = addKeywordForm()
    return render_template('index.html',
                            form=form)
