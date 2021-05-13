"""Main application package"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user
from flask_migrate import Migrate
from flask_principal import Principal, identity_loaded, RoleNeed, UserNeed
import os

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
principal = Principal()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or os.environ.get('SQLALCHEMY_DATABASE_URI'),
        SQLALCHEMY_TRACK_MODIFICATIONS=os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS'),
        SESSION_COOKIE_SECURE=os.environ.get('SESSION_COOKIE_SECURE')
    )
    db.init_app(app)

    bcrypt.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = "customer.login"
    login_manager.login_message_category = "info"

    principal.init_app(app)

    migrate.init_app(app, db)

    with app.app_context():
        @identity_loaded.connect_via(app)
        def on_identity_loaded(sender, identity):
            # Set the identity user object
            identity.user = current_user

            # Add the UserNeed to the identity
            if hasattr(current_user, 'id'):
                identity.provides.add(UserNeed(current_user.id))

            # Assuming the User model has a list of roles, update the
            # identity with the roles that the user provides
            if hasattr(current_user, 'roles'):
                for role in current_user.roles:
                    identity.provides.add(RoleNeed(role.name))

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
            return render_template('error_pages/404.html'), 404

        @app.errorhandler(403)
        def permission_denied(e):
            return render_template('error_pages/403.html'), 403

        @app.errorhandler(500)
        def server_error(e):
            return render_template('error_pages/500.html'), 500

        return app
