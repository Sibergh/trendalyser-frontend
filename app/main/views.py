from flask import render_template, redirect, url_for
from app import app
from .forms import addKeywordForm

@app.route('/')
def index():
    form = addKeywordForm()
    return render_template('index.html')

@app.route('/managekeywords', methods=['GET', 'POST'])
def managekeywords():
        form = addKeywordForm()
        if form.validate_on_submit():
            return redirect(url_for('managekeywords'))
        return render_template('managekeywords.html',
                                form=form)
