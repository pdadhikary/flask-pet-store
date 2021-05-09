from flask import Blueprint, render_template, request, url_for
from flask_pet_store.models import Product

product_blueprint = Blueprint('products', __name__, template_folder='templates')


# TODO: get popular brands with most sales
def get_brands():
    return Product.query.group_by(Product.brand).limit(5).all()


@product_blueprint.route('/')
def index():
    page = request.args.get('page', default=1, type=int)
    brand = request.args.get('brand', default=None, type=str)

    products = Product.query
    if brand:
        products = products.filter_by(brand=brand).paginate(per_page=6, page=page)
    else:
        products = products.paginate(per_page=6, page=page)

    return render_template('product/index.html', products=products, brands=get_brands(), current_brand=brand)
