from flask import Blueprint, render_template, url_for, redirect, request, flash, abort, current_app
from flask_pet_store import db
from flask_pet_store.models import Product
from flask_pet_store.admin.forms import ProductDeleteForm, ProductUpsertForm
from PIL import Image
import os
import secrets

admin_blueprint = Blueprint('admin', __name__, template_folder='templates')
product_image_upload = os.path.join('static', 'img', 'uploads', 'product_images')


@admin_blueprint.route('/')
def index():
    return render_template('admin/index.html')


def delete_product_image(image_name):
    try:
        if image_name and image_name != 'default.jpg':
            os.remove(os.path.join(current_app.root_path, product_image_upload, image_name))
    except OSError as error:
        print(f'File could not be deleted: {error}')


def save_product_image(form_image):
    # generate random file name
    random_token = secrets.token_urlsafe(12)
    _, f_ext = os.path.splitext(form_image.filename)
    image_name = random_token + f_ext
    image_path = os.path.join(current_app.root_path, product_image_upload, image_name)
    # resize image
    output_size = (256, 256)
    i = Image.open(form_image)
    i.thumbnail(output_size)
    i.save(image_path)

    return image_name


@admin_blueprint.route('/products/upsert/<int:prodId>', methods=['GET', 'POST'])
def upsert_product(prodId):
    product = Product.query.get_or_404(prodId)
    # Insert request
    if prodId == 0:
        product = Product()

    edit_form = ProductUpsertForm(obj=product)
    if edit_form.validate_on_submit():
        product.name = edit_form.name.data
        product.price = edit_form.price.data
        product.brand = edit_form.brand.data
        product.category = edit_form.category.data
        product.quantity = edit_form.quantity.data
        product.description = edit_form.description.data
        if edit_form.product_image_file.data:
            print(edit_form.product_image_file.data)
            image_name = save_product_image(edit_form.product_image_file.data)
            delete_product_image(product.product_image)
            product.product_image = image_name
        # Insert request
        if prodId == 0:
            db.session.add(product)
        db.session.commit()
        flash(message='Product successfully updated and inserted', category='success')
        return redirect(url_for('admin.manage_products'))
    return render_template('admin/upsert_product.html', edit_form=edit_form, product=product)


@admin_blueprint.route('/products', methods=['GET', 'POST'])
def manage_products():
    if request.method == "POST":
        prodId = request.form.get('product_id')
        product_to_delete = Product.query.get(prodId)
        if product_to_delete:
            delete_product_image(product_to_delete.product_image)
            db.session.delete(product_to_delete)
            db.session.commit()
            flash(message='Product successfully deleted!', category='success')
            return redirect(url_for('admin.manage_products'))
        flash(message='Product cannot be found...', category='warning')
        return abort(404)
    if request.method == "GET":
        delete_form = ProductDeleteForm()
        products = Product.query.all()
        return render_template('admin/products.html', products=products, delete_form=delete_form)
