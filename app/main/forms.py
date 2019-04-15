from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class SearchForm(FlaskForm):

    search = StringField(validators=[Required()])
    submit = SubmitField('Submit')