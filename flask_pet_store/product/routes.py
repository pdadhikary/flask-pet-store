from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_pet_store.models import db, Product
from flask_pet_store.product.forms import SearchForm
from sqlalchemy import or_, func
from decimal import Decimal

product_blueprint = Blueprint('products', __name__, template_folder='templates')


def get_brands():
    brands = db.session.query(Product.brand).group_by(Product.brand).order_by(
        func.count().desc()).limit(5).all()
    brands = [x[0] for x in brands]
    return brands


def getProductsFromCart():
    itemsInCart = session['cart'] if 'cart' in session else {}
    cart = []
    for product_id, data in itemsInCart.items():
        product = Product.query.get(product_id)
        unit_price = Decimal(str(product.price))
        quantity = Decimal(str(data['quantity']))
        total = unit_price * quantity
        cart.append({'id': product_id,
                     'name': product.name,
                     'img': product.product_image,
                     'brand': product.brand,
                     'unit_price': unit_price,
                     'quantity': quantity,
                     'total': total})
    return cart


@product_blueprint.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', default=1, type=int)
    brand = request.args.get('brand', default=None, type=str)
    q = request.args.get('q', default=None, type=str)

    search_form = SearchForm(search_query=q)

    if search_form.validate_on_submit():
        return redirect(url_for('products.index',
                                q=search_form.search_query.data,
                                brand=brand))

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


@product_blueprint.route('/checkout')
def checkout():
    cart = getProductsFromCart()

    sum_price = Decimal('0.00')
    for product in cart:
        sum_price += product['total']

    return render_template('product/checkout.html', cart=cart, sum_price=sum_price)


@product_blueprint.route('/checkout/add', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('id')
    quantity = request.form.get('quantity') or 1

    if product_id:
        product = Product.query.get(product_id)
        cartItem = {product_id: {'quantity': quantity}}
        if 'cart' not in session:
            session['cart'] = {}
        session['cart'] = session['cart'] | cartItem
        flash(message=f'{product.name[:50] + "..."} successfully added to cart!', category='success')
    else:
        flash(message='Couldn\'t add this product to cart...', category='danger')
    return redirect(request.referrer)


@product_blueprint.route('/checkout/remove', methods=['POST'])
def remove_form_cart():
    product_id = request.form.get('id')
    if 'cart' in session and product_id in session['cart']:
        session.modified = True
        session['cart'].pop(product_id, None)
    return redirect(request.referrer)
