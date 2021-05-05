from flask_wtf import FlaskForm
from flask_pet_store.models import User
from wtforms import StringField, PasswordField, SubmitField, SelectField, ValidationError
from wtforms.validators import Length, EqualTo, Email, DataRequired, Regexp


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        customer = User.query.filter_by(username=username_to_check.data).first()
        if customer:
            raise ValidationError(message="Username already exists! Please try a different Username.")

    def validate_email(self, email_address_to_check):
        customer = User.query.filter_by(email=email_address_to_check.data).first()
        if customer:
            raise ValidationError(message="Email address is already in use! Try a different one.")

    first_name = StringField(label='First Name', validators=[DataRequired(message="Please enter your First Name.")])
    last_name = StringField(label='Last Name', validators=[DataRequired(message="Please enter your Last name.")])
    email = StringField(label='Email Address', validators=[DataRequired(message="Please enter your Email Address"),
                                                           Email(message="Email Address is not valid.")])
    sex = SelectField(label='Sex', choices=[('Male', 'Male'), ('Female', 'Female'), ('X', 'X')],
                      validators=[DataRequired("Please choose your sex.")])
    username = StringField(label='Username',
                           validators=[DataRequired(message="Please enter a Username."),
                                       Length(min=1, max=60, message="Username must be between 1 and 60 characters")])
    password1 = PasswordField(label='Password', validators=[
        DataRequired("Please choose a Password."),
        Length(min=6, message="Password must have at least 6 characters")
    ])
    password2 = PasswordField(label='Confirm Password',
                              validators=[DataRequired("Please confirm your Password"),
                                          EqualTo('password1', message='Passwords must match.')])
    street_name = StringField(label='Street Address',
                              validators=[DataRequired("Please enter your Street Address")])
    city = StringField(label='City', validators=[DataRequired(message="Please enter your City Name")])
    province = SelectField(label='Province', choices=[
        ('ON', 'ON'),
        ('BC', 'BC'),
        ('QC', 'QC'),
        ('MB', 'MB'),
        ('AB', 'AB'),
        ('SK', 'SK'),
        ('NL', 'NL'),
        ('PE', 'PE'),
        ('NS', 'NS'),
        ('NB', 'NB'),
        ('YT', 'YT'),
        ('NT', 'NT'),
        ('NU', 'NU'),
    ], validators=[DataRequired(message="Please choose your Province of residence")])
    zip_code = StringField(label='Zip Code',
                           validators=[
                               DataRequired(message="Please enter your Canadian Zip Code"),
                               Regexp(regex="^[A-Za-z][0-9][A-Za-z][ ]?[0-9][A-Za-z][0-9]$",
                                      message="Zip Code is not valid.")
                           ])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(message="Please enter your Username")])
    password = PasswordField(label="Password", validators=[DataRequired(message="Please enter your Password")])
    submit = SubmitField(label="Login")
