from flask import Blueprint, render_template, url_for

product_blueprint = Blueprint('products', __name__, template_folder='templates')


@product_blueprint.route('/')
def index():
    return render_template('product/index.html')
