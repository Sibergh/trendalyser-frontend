from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class addKeywordForm(Form):
    keyword = StringField('keyword', validators=[DataRequired()])
