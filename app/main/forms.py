from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class addKeywordForm(Form):
    keyword = StringField('keyword', validators=[Required()])
    submit = SubmitField('Add')
