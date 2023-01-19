from app.extensions import ma

class UserSchema (ma.Schema):
    id = ma.Integer(dump_only=True)
    username = ma.String(required = True)
    tipo = ma.String(required = True)

class ProductSchema(ma.Schema):
    id = ma.Integer()
    tipo = ma.String(required = True)
    preço = ma.Integer(required = True)
    tamanho = ma.String(required = True)
    quantidade = ma.Integer(required = True)