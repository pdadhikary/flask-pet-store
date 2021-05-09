from flask import Blueprint, render_template, request, url_for
from flask_pet_store.models import Product

product_blueprint = Blueprint('products', __name__, template_folder='templates')


@product_blueprint.route('/')
def index():
    page = request.args.get(key='page', default=1, type=int)
    products = Product.query.paginate(per_page=6, page=page)
    return render_template('product/index.html', products=products)
