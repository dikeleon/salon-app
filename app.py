from flask import Flask
from database import database

# blueprint import
from apps.products.views import products
from apps.users.views import users

def create_app():
    app = Flask(__name__)
    # setup with the configuration provided
    app.config.from_object('config.DevelopmentConfig')
    
    # setup all our dependencies
    database.init_app(app)
    
    # register blueprint
    app.register_blueprint(users, url_prefix="/users")
    app.register_blueprint(products, url_prefix="/products")
    
    return app

if __name__ == "__main__":
    create_app().run()