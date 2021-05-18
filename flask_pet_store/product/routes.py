from flask import Blueprint, render_template, request, redirect, url_for
from flask_pet_store.models import db, Product
from flask_pet_store.product.forms import SearchForm
from sqlalchemy import or_, func

product_blueprint = Blueprint('products', __name__, template_folder='templates')


def get_brands():
    brands = db.session.query(Product.brand).group_by(Product.brand).order_by(func.count().desc()).limit(5).all()
    brands = [x[0] for x in brands]
    return brands


@product_blueprint.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', default=1, type=int)
    brand = request.args.get('brand', default=None, type=str)
    q = request.args.get('q', default=None, type=str)

    search_form = SearchForm(search_query=q)

    if search_form.validate_on_submit():
        return redirect(url_for('products.index', q=search_form.search_query.data, brand=brand))

    # filter products using arguments
    products = Product.query
    if q:
        products = products.filter(or_(Product.name.ilike(f'%{q}%'),
                                       Product.brand.ilike(f'%{q}%'),
                                       Product.description.ilike(f'%{q}%')))
    if brand:
        products = products.filter_by(brand=brand)
    products = products.paginate(per_page=6, page=page)

    return render_template('product/index.html', search_form=search_form,
                           products=products, brands=get_brands(),
                           q=q, brand=brand)


@product_blueprint.route('/cart/add', methods=['POST'])
def add_to_cart():
    print({
        'id': request.form.get('id'),
        'quantity': request.form.get('quantity')
    })
    return redirect(request.referrer)
