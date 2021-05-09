from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange


class ProductUpsertForm(FlaskForm):
    name = StringField(label='Product Name*', validators=[DataRequired(message='Product Name cannot be empty.')])
    price = DecimalField(label='Price', places=2, validators=[DataRequired(message='Please enter a valid price.')])
    brand = StringField(label='Brand Name*', validators=[DataRequired(message='Brand Name cannot be empty.')])
    category = StringField(label='Category*',
                           validators=[DataRequired(message='Category cannot be empty.')])
    quantity = IntegerField(label='Quantity*',
                            validators=[DataRequired(message='Quantity must be an number.'),
                                        NumberRange(min=1, message='Quantity cannot be negative')])
    description = TextAreaField(label='Product Description*',
                                validators=[
                                    DataRequired(message='Product Description cannot be empty.'),
                                    Length(max=350,
                                           message='Description cannot be longer than 350 characters.')
                                ])
    product_image_file = FileField(label='Product Thumbnail', validators=[
        FileAllowed(['jpeg', 'jpg', 'png'], message="File must be an image: .jpg, .jpeg or .png")])
    submit = SubmitField(label='Save Changes')


class ProductDeleteForm(FlaskForm):
    submit = SubmitField(label='Delete')
