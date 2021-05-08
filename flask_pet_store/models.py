from flask_pet_store import db, bcrypt, login_manager
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


product_orders = db.Table(
    'product_orders',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'))
)


class User(db.Model, UserMixin):
    id = db.Column(
        db.Integer(), primary_key=True
    )
    _first_name = db.Column(
        'first_name', db.String(length=30), nullable=False
    )
    _last_name = db.Column(
        'last_name', db.String(length=30), nullable=False
    )
    sex = db.Column(
        db.String(length=1), nullable=False
    )
    _email = db.Column(
        'email', db.String(length=80), nullable=False, unique=True
    )
    username = db.Column(
        db.String(length=60), nullable=False, unique=True
    )
    _password_hash = db.Column(
        'password_hash', db.String(length=60), nullable=False
    )
    _street_name = db.Column(
        'street_name', db.String(length=60), nullable=False
    )
    _zip_code = db.Column(
        'zip_code', db.String(length=7), nullable=False
    )
    _city = db.Column(
        'city', db.String(length=30), nullable=False
    )
    province = db.Column(
        db.String(length=2), nullable=False
    )
    orders = db.relationship('Product', secondary=product_orders, backref=db.backref('ordered_by', lazy='dynamic'))

    @hybrid_property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, entered_name):
        self._first_name = entered_name.title()

    @hybrid_property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, entered_name):
        self._last_name = entered_name.title()

    @hybrid_property
    def email(self):
        return self._email

    @email.setter
    def email(self, entered_email):
        self._email = entered_email.lower()

    @hybrid_property
    def password(self):
        return self._password_hash

    @password.setter
    def password(self, plain_text_password):
        self._password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    @hybrid_property
    def street_name(self):
        return self._street_name

    @street_name.setter
    def street_name(self, entered_street):
        self._street_name = entered_street.title()

    @hybrid_property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, entered_zip):
        formatted_zip = entered_zip
        if entered_zip[3] != ' ':
            formatted_zip = entered_zip[:3] + ' ' + entered_zip[3:]
        self._zip_code = formatted_zip.upper()

    @hybrid_property
    def city(self):
        return self._city

    @city.setter
    def city(self, entered_city):
        self._city = entered_city.title()

    def verify_password(self, input_password):
        return bcrypt.check_password_hash(self._password_hash, input_password)

    def __repr__(self):
        return f'<User> {self.last_name}, {self.first_name}'


class Product(db.Model):
    id = db.Column(
        db.Integer(), primary_key=True
    )
    _name = db.Column(
        'name', db.String(length=60), nullable=False
    )
    _brand = db.Column(
        'brand', db.String(length=60), nullable=False
    )
    _category = db.Column(
        'category', db.String(length=30), nullable=False
    )
    product_image = db.Column(
        db.String(length=150), nullable=True
    )
    quantity = db.Column(
        db.Integer(), nullable=False
    )
    description = db.Column(
        db.String(length=350), nullable=False
    )

    @hybrid_property
    def name(self):
        return self._name

    @name.setter
    def name(self, entered_name):
        self._name = entered_name.strip().title()

    @hybrid_property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, entered_brand):
        self._brand = entered_brand.strip().title()

    @hybrid_property
    def category(self):
        return self._category

    @category.setter
    def category(self, entered_category):
        self._category = entered_category.strip().title()

    def __repr__(self):
        return f'<Product> {self.name}'
