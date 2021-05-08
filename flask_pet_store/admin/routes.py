from flask import Blueprint, render_template, url_for, redirect, request, flash, abort
from flask_pet_store import db
from flask_pet_store.models import Product
from flask_pet_store.admin.forms import ProductDeleteForm, ProductEditForm

admin_blueprint = Blueprint('admin', __name__, template_folder='templates')


@admin_blueprint.route('/')
def index():
    return render_template('admin/index.html')


@admin_blueprint.route('/products/<prodId>', methods=['GET', 'POST'])
def edit_product(prodId):
    product = Product.query.get(prodId)
    if product:
        edit_form = ProductEditForm(obj=product)
        if edit_form.validate_on_submit():
            product.name = edit_form.name.data
            product.brand = edit_form.brand.data
            product.category = edit_form.category.data
            product.quantity = edit_form.quantity.data
            product.description = edit_form.description.data
            db.session.commit()
            flash(message='Product successfully updated', category='success')
            return redirect(url_for('admin.manage_products'))
        if edit_form.errors != {}:
            for err_msg in edit_form.errors.values():
                msg = ", ".join(err_msg)
                flash(message=f'Could not update product: {msg}', category='danger')
        return render_template('admin/edit_product.html', edit_form=edit_form, product=product)
    flash(message='Product cannot me found...', category='warning')
    return abort(status=404)


@admin_blueprint.route('/products', methods=['GET', 'POST'])
def manage_products():
    if request.method == "POST":
        print(f"Item Deleted: {request.form.get('product_name')}")
        return redirect(url_for('admin.manage_products'))

    if request.method == "GET":
        delete_form = ProductDeleteForm()
        products = Product.query.all()
        return render_template('admin/products.html', products=products, delete_form=delete_form)
