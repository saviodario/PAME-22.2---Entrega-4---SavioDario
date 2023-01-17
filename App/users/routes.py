from flask import Blueprint
from .controller import UserController,UserDetails,ProductController,ProductDetails

user_api = Blueprint("user_api",__name__)
product_api = Blueprint("product_api",__name__)
""" a estrutura primeira /users/idu serve para saber quem esta mexendo no programa, de forma
a filtrar os poderes do gerente"""
user_api.add_url_rule(
    "/users/<int:idu>",
    view_func= UserController.as_view("users_controller"),
    methods = ["POST","GET"]
)

product_api.add_url_rule(
    "/users/<int:idu>/products",
    view_func= ProductController.as_view("products_controller"),
    methods = ["POST","GET"]
)

user_api.add_url_rule(
    "/users/<int:idu>/users/<int:id>",
    view_func= UserDetails.as_view("users_details"),
    methods = ["GET","PUT","PATCH","DELETE"]
)

product_api.add_url_rule(
    "/users/<int:idu>/products/<int:idp>",
    view_func= ProductDetails.as_view("products_details"),
    methods = ["GET","PUT","PATCH","DELETE"]
)