from flask import Flask, render_template, redirect, request, flash, session

from flask_app import app
from flask_app.models.user import PreUser
from flask_app.models.product import Product
from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

# land page
@app.route('/')
def index():
    products = Product.get_all()
    return render_template('index.html', products=products)

# product page 
@app.route('/product/<int:product_id>')
def product_page(product_id):
    product = Product.get_by_id(product_id)
    products = Product.get_all()
    if product:
        return render_template('product_page.html', product=product, products=products)
    else:
        # Handle case when product is not found
        return "Product not found", 404

@app.route('/view_all')
def view_all_page_display():
    products=Product.get_all()
    return render_template('view_all.html', products=products)