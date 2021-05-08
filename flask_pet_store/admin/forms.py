from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class ProductUpsertForm(FlaskForm):
    name = StringField(label='Product Name', validators=[DataRequired(message='Product Name cannot be empty.')])
    brand = StringField(label='Brand Name', validators=[DataRequired(message='Brand Name cannot be empty.')])
    category = StringField(label='Category',
                           validators=[DataRequired(message='Category cannot be empty.')])
    quantity = IntegerField(label='Quantity',
                            validators=[DataRequired(message='Quantity cannot be empty.'),
                                        NumberRange(min=1, message='Quantity cannot be negative')])
    description = TextAreaField(label='Product Description',
                                validators=[
                                    DataRequired(message='Product Description cannot be empty.'),
                                    Length(max=350,
                                           message='Description cannot be longer than 350 characters.')
                                ])
    submit = SubmitField(label='Save Changes')


class ProductDeleteForm(FlaskForm):
    submit = SubmitField(label='Delete')
