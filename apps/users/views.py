from flask import Blueprint, render_template
users = Blueprint('users', __name__, template_folder="templates")

@users.route("/")
def users_index():
    return render_template('users/index.html')

@users.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404