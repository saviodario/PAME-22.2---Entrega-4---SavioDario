from flask import Blueprint
from .controller import UserController,UserDetails,ProductController,ProductDetails,UserBuyng

user_api = Blueprint("user_api",__name__)
product_api = Blueprint("product_api",__name__)
buy_api = Blueprint("buy_api",__name__)

""" a estrutura primeira /<int:idu> serve para saber quem esta mexendo no programa, de forma
a filtrar os poderes do gerente"""

user_api.add_url_rule(
    "/<int:idu>/users",
    view_func= UserController.as_view("users_controller"),
    methods = ["POST","GET"]
)
""" POST:se idu pertense a um gerente, será adicionado um user aos dados
    GET: retorna todos os users independente de ser gerente ou cliente"""

product_api.add_url_rule(
    "/<int:idu>/products",
    view_func= ProductController.as_view("products_controller"),
    methods = ["POST","GET"]
)
""" POST:se idu pertense a um gerente, será adicionado um produto aos dados
    GET: retorna todos os produtos independente de ser gerente ou cliente"""

user_api.add_url_rule(
    "/<int:idu>/users/<int:id>",
    view_func= UserDetails.as_view("users_details"),
    methods = ["GET","PUT","PATCH","DELETE"]
)
""" GET: retorna o user de id = id
    PUT: se idu pertencer a gerente, altera todos os dados de um usuário
    PATCH: se idu pertence a gerente, altera parcialmente os dados de um usuário
    DELETE: se idu pertence a gerente, deleta um usuário"""


product_api.add_url_rule(
    "/<int:idu>/products/<int:idp>",
    view_func = ProductDetails.as_view("products_details"),
    methods = ["GET","PUT","PATCH","DELETE"]
)
""" GET: retorna o produto de id = idp
    PUT: se idu pertencer a gerente, altera todos os dados de um produto
    PATCH: se idu pertence a gerente, altera parcialmente os dados de um produto
    DELETE: se idu pertence a gerente, deleta um produto"""

buy_api.add_url_rule(
    "/<int:idu>/buy/products/<int:idp>/",
    view_func = UserBuyng.as_view('user_buyng'),
    methods = ["PATCH"]
)
""" Se idu pertence a um cliente, o cliente de id = idu irá comprar o produto de id = ipd
    subtraindo a quantia do produto e retornando uma mensagem informando o nome de 
    quem comprou e o valor do produto."""