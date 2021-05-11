from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SearchForm(FlaskForm):
    search_query = StringField(label='Query')
    submit = SubmitField(label='Search')
