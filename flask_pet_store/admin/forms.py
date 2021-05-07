from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField
from wtforms.validators import DataRequired


class ProductEditForm(FlaskForm):
    name = StringField(label='Product Name', validators=[DataRequired(message='Please enter product name.')])
    brand = StringField(label='Brand', validators=[DataRequired(message='Please enter the brand name.')])
    category = SelectField(label='Category',
                           default='Choose a Category',
                           description='Choose a category',
                           choices=['Canned Food', 'Pond Care', 'Pond Care', 'Pet Bird Food', 'Dry Food'],
                           validators=[DataRequired(message='Please select a category.')])
    quantity = IntegerField(label='Quantity', validators=[DataRequired(message='Please enter the quantity in store.')])
    description = TextAreaField(label='Product Description',
                                validators=[DataRequired(message='Please enter the description of the product')])
