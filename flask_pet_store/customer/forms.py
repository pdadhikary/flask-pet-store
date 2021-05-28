from flask_wtf import FlaskForm
from flask_pet_store.models import User
from wtforms import StringField, PasswordField, SubmitField, SelectField, ValidationError
from wtforms.validators import Length, EqualTo, Email, DataRequired, Regexp


class CustomerForm(FlaskForm):
    def validate_username(self, username_to_check):
        customer = User.query.filter_by(username=username_to_check.data).first() or User.query.filter_by(
            email=username_to_check.data).first()
        if customer and customer.id != self.current_id:
            raise ValidationError(message="Username already exists! Please try a different Username.")

    def validate_email(self, email_address_to_check):
        customer = User.query.filter_by(email=email_address_to_check.data).first()
        if customer:
            raise ValidationError(message="Email address is already in use! Try a different one.")

    current_id = None
    first_name = StringField(label='First Name*', validators=[DataRequired(message="First Name cannot be empty.")])
    last_name = StringField(label='Last Name*', validators=[DataRequired(message="Last name cannot be empty.")])
    sex = SelectField(label='Sex*', choices=[('M', 'Male'), ('F', 'Female'), ('X', 'X')],
                      validators=[DataRequired("Please choose your sex.")])
    username = StringField(label='Username*',
                           validators=[DataRequired(message="Username cannot be empty."),
                                       Length(min=1, max=60, message="Username must be between 1 and 60 characters")])
    street_name = StringField(label='Street Address*',
                              validators=[DataRequired("Please enter your Street Address")])
    city = StringField(label='City*', validators=[DataRequired(message="Please enter your City Name")])
    province = SelectField(label='Province*', choices=[
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
    zip_code = StringField(label='Zip Code*',
                           validators=[
                               DataRequired(message="Please enter your Canadian Zip Code"),
                               Regexp(regex="^[A-Za-z][0-9][A-Za-z][ ]?[0-9][A-Za-z][0-9]$",
                                      message="Zip Code is not valid.")
                           ])


class UpdateForm(CustomerForm):
    verify_password = PasswordField(label='Enter Your Password to Proceed*', validators=[
        DataRequired("Please enter your password in order to complete update process.")
    ])
    submit = SubmitField(label='Update Account')


class RegisterForm(CustomerForm):
    email = StringField(label='Email Address*', validators=[DataRequired(message="Email Address cannot be empty."),
                                                            Email(message="Email Address is not valid.")])
    password1 = PasswordField(label='Password*', validators=[
        DataRequired("Password cannot be empty."),
        Length(min=6, message="Password must have at least 6 characters")
    ])
    password2 = PasswordField(label='Confirm Password*',
                              validators=[DataRequired("Please confirm your Password"),
                                          EqualTo('password1', message='Passwords do not match.')])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    login_name = StringField(label="Username or Email Address",
                             validators=[DataRequired(message="Please enter your Username/Email Address")])
    password = PasswordField(label="Password", validators=[DataRequired(message="Please enter your Password")])
    submit = SubmitField(label="Login")
