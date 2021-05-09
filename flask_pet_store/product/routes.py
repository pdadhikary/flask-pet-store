from flask import Blueprint, render_template, url_for
from flask_pet_store.models import Product

product_blueprint = Blueprint('products', __name__, template_folder='templates')


@product_blueprint.route('/')
def index():
    products = Product.query.all()
    return render_template('product/index.html', products=products)
