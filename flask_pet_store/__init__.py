"""Main application package"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "customer.login"
login_manager.login_message_category = "info"

migrate = Migrate(app, db)

from flask_pet_store.customer.routes import customer_blueprint
from flask_pet_store.product.routes import product_blueprint
from flask_pet_store.admin.routes import admin_blueprint

app.register_blueprint(customer_blueprint, url_prefix='/customer')
app.register_blueprint(product_blueprint, url_prefix='/products')
app.register_blueprint(admin_blueprint, url_prefix='/admin')


# home page
@app.route('/')
def home_page():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
