from flask import Flask
from App.users.routes import user_api
from App.users.routes import product_api
from App.users.routes import buy_api

def creat_app():
    app = Flask(__name__)
    
    app.register_blueprint(user_api)
    app.register_blueprint(product_api)
    app.register_blueprint(buy_api)
    
    return app