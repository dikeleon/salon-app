from flask import Blueprint, render_template
products = Blueprint('products', __name__, template_folder="templates")

@products.route("/")
def products_index():
    return render_template('products/index.html')

@products.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404