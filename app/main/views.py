from flask import Flask, render_template, flash, redirect, url_for
from . import main
from .. import db
from .forms import *
from .models import Keyword

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/managekeywords', methods=['GET', 'POST'])
def managekeywords():
        form = addKeywordForm()
        if form.validate_on_submit():
            newkeyword = Keyword(keyword=form.keyword.data)
            newkeyword.save()
            flash('New keyword added')
            form.keyword.data = ''
            return redirect(url_for('.managekeywords'))
        return render_template('managekeywords.html',
                                form=form, wordlist=getkeywords())


def getkeywords():
    wordlist = []
    for keyword in Keyword.objects:
        wordlist.append(keyword)

    return wordlist
