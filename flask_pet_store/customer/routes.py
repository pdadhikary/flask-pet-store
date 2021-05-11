from flask import Blueprint, render_template, redirect, \
    url_for, flash, current_app, session
from flask_pet_store import db
from flask_pet_store.models import User, Role
from flask_pet_store.customer.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required
from flask_principal import Identity, AnonymousIdentity, identity_changed

customer_blueprint = Blueprint('customer', __name__, template_folder='templates')


# TODO: Add functionality to update Customer Info
@customer_blueprint.route('/')
@login_required
def index():
    return render_template('customer/index.html')


@customer_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            sex=form.sex.data,
            email=form.email.data,
            username=form.username.data,
            password=form.password1.data,
            street_name=form.street_name.data,
            zip_code=form.zip_code.data,
            city=form.city.data,
            province=form.province.data
        )

        # Assign role to customer
        customer_role = Role.query.filter_by(name='customer').first()
        user_to_create.roles.append(customer_role)
        # Add customer to database
        db.session.add(user_to_create)
        db.session.commit()

        login_user(user_to_create)
        flash(message=f"Account successfully created! You are now logged in as: {user_to_create.username}",
              category="success")
        return redirect(url_for('customer.index'))

    return render_template('customer/register.html', form=form)


@customer_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        customer = User.query.filter_by(username=form.username.data).first()
        if customer and customer.verify_password(
                input_password=form.password.data
        ):
            login_user(customer)
            flash(message=f"You are now logged in as: {customer.username}", category="success")
            identity_changed.send(current_app._get_current_object(),
                                  identity=Identity(customer.id))
            return redirect(url_for('products.index'))
        else:
            flash(message=f"Incorrect Username and/or Password! Please try again.", category="warning")
    return render_template('customer/login.html', form=form)


@customer_blueprint.route('/logout')
def logout():
    # Remove the user information from the session
    logout_user()
    # Remove session keys set by Flask-Principal
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)
    # Tell Flask-Principal the user is anonymous
    identity_changed.send(current_app._get_current_object(),
                          identity=AnonymousIdentity())

    flash(message="You have been logged out", category="info")
    return redirect(url_for('customer.login'))
