from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

bp = Blueprint('product', __name__)


@bp.route('/')
def home():
    return render_template('home.html')


@bp.route('/about')
def about():
    return render_template('about.html')


@bp.route('/products')
def products():
    return render_template('products.html')


@bp.route('/create_product')
def create_product():
    return render_template('create_product.html')