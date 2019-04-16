from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class SearchForm(FlaskForm):

    search = StringField('Search for News',validators=[Required()])
    submit = SubmitField('Search')