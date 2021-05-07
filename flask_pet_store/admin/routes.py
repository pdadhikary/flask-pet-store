from flask import Blueprint, render_template, url_for
from flask_pet_store.models import Product
from flask_pet_store.admin.forms import ProductEditForm

admin_blueprint = Blueprint('admin', __name__, template_folder='templates')


@admin_blueprint.route('/')
def index():
    return render_template('admin/index.html')


@admin_blueprint.route('/products', methods=['GET', 'POST'])
def manage_products():
    # editForm = ProductEditForm()
    products = Product.query.all()
    return render_template('admin/products.html', products=products)
