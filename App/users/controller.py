from flask import request
from flask.views import MethodView
from .models import my_users as users
from .models import my_products as products
from .schemas import UserSchema
from .schemas import ProductSchema

def get_last_id_user():
    last_user = users[-1]
    return last_user['id']

def get_last_id_product():
    last_product = products[-1]
    return last_product['id']

class UserController(MethodView):
    def post(self,idu):
        for user in users:
            if user['id'] == idu and user['tipo'] == 'gerente':
                schema = UserSchema()
                data = request.json
                
                data['id'] = get_last_id_user() + 1
                
                try:
                    user = schema.dump(data)
                    users.append(user)
                except:
                    print('erro')
                    return {"msg":"erro do cliente"},400
                return user, 201
        return {'msg':'Precisa ser gerente para fazer tal requisição'},404
    
    def get(self,idu):
        for user in users:
            if user['id'] == idu:
                schema = UserSchema()
                return schema.dump(users, many=True), 200
        return {"msg":"Não existe tal usuário"},404
    
class UserDetails(MethodView):
    def get(self,idu,id):
        schema = UserSchema()
        for user in users:
            if user['id'] == id:
                return schema.dump(user), 200
        return {"msg":"Não existe tal usuário"},404
    
    def put(self,idu,id):
        for user in users:
            if user['id'] == idu and user['tipo'] == 'gerente':
                schema = UserSchema()
                data = request.json
                userindex = -1
                for user in users:
                    if user['id'] == id:
                        userindex = users.index(user)
                if userindex == -1:
                    return {},404
                data["id"] = id
                newuser = schema.dump(data)
                users[userindex] = newuser
                return newuser,201
        return {'msg':'Precisa ser gerente para fazer tal requisição'},404
    
    def patch(self,idu,id):
        for user in users:
            if user['id'] == idu and user['tipo'] == 'gerente':
                schema = UserSchema()
                data = request.json
                userIndex = -1
                for user in users:
                    if user["id"] == id:
                        userIndex = users.index(user)
                if userIndex == -1:
                    return {}, 404
                user = users[userIndex]
                username = data.get('username',user['username'])
                tipo = data.get('tipo', user['tipo'])
                data['username'] = username
                data['tipo'] = tipo
                data['id'] = id
                user =schema.dump(data)
                users[userIndex] = user
                return user, 201
        return {'msg':'Precisa ser gerente para fazer tal requisição'},404
    
    def delete(self, idu,id):
        for user in users:
            if user['id'] == idu and user['tipo'] == 'gerente':
                for user in users:
                    if user['id'] == id:
                        nome = user['username']
                        users.remove(user)
                        return {'msg':f'O usuário {nome} foi removido do sistema'},204
                return{'msg':f'O usuário de id {id} não consta no sistema'},404
        return {'msg':'Precisa ser gerente para fazer tal requisição'},404
            
class ProductController(MethodView):
    def post(self,idu):
        for user in users:
            if user['id'] == idu and user['tipo'] == 'gerente':
                schema = ProductSchema()
                data = request.json
                
                data['id'] = get_last_id_product() + 1
                
                try:
                    product = schema.dump(data)
                    products.append(product)
                except:
                    print('erro')
                    return {"msg":"erro do cliente"},400
                return product, 201
        return {'msg':'Precisa ser gerente para fazer tal requisição'},404
    
    def get(self,idu):
        for user in users:
            if user['id'] == idu:
                schema = ProductSchema()
                return schema.dump(products, many=True), 200
        return {"msg":"Não existe tal usuário"},404
    
class ProductDetails(MethodView):
    def get(self,idu,idp):
        schema = ProductSchema()
        for product in products:
            if product['id'] == idp:
                return schema.dump(product), 200
        return {"msg":"Não existe tal produto"},404
    
    def put(self,idu,idp):
        for user in users:
            if user['id'] == idu and user['tipo'] == 'gerente':
                schema = ProductSchema()
                data = request.json
                productindex = -1
                for product in products:
                    if product['id'] == idp:
                        productindex = products.index(product)
                if productindex == -1:
                    return {},404
                data["id"] = idp
                newproduct = schema.dump(data)
                products[productindex] = newproduct
                return newproduct,201
        return {'msg':'Precisa ser gerente para fazer tal requisição'},404
    def patch(self,idu,idp):
        for user in users:
            if user['id'] == idu and user['tipo'] == 'gerente':
                schema = ProductSchema()
                data = request.json
                productIndex = -1
                for product in products:
                    if product["id"] == idp:
                        productIndex = products.index(product)
                if productIndex == -1:
                    return {}, 404
                product = products[productIndex]
                tamanho = data.get('tamanho',product['tamanho'])
                tipo = data.get('tipo', product['tipo'])
                preço = data.get('preço',product['preço'])
                quantidade = data.get('quantidade',product['quantidade'])
                data['tamanho'] = tamanho
                data['tipo'] = tipo
                data['id'] = idp
                data['preço'] = preço
                data['quantidade'] = quantidade
                product =schema.dump(data)
                products[productIndex] = product
                return product, 201
        return {'msg':'Precisa ser gerente para fazer tal requisição'},404
    
    def delete(self,idu,idp):
        for user in users:
            if user['id'] == idu and user['tipo'] == 'gerente':
                for product in products:
                    if product['id'] == idp:
                        products.remove(product)
                        return {'msg':f'O produto de id {idp} foi removido do sistema'},204
                return{'msg':f'O produto de id {idp} não consta no sistema'},404
        return {'msg':'Precisa ser gerente para fazer tal requisição'},404

class UserBuyng(MethodView):
    def patch(self,idu,idp):
        for user in users:
            if user['id'] == idu and user['tipo'] == 'cliente':
                userIndex = users.index(user)
                user = users[userIndex]
                nome = user['username'] 
                productIndex = -1
                for product in products:
                    if product["id"] == idp:
                        productIndex = products.index(product)
                if productIndex == -1:
                    return {'msg':'esse produto não existe'}, 404
                product = products[productIndex]
                if product['quantidade'] <= 0: #verifica se o produto que esta sendo comprado já esta esgotado
                    return {'msg':'produto esgotado'} 
                product['quantidade'] = product['quantidade'] - 1 #subtrai a quantia de produtos em estoque
                tipo = product['tipo']
                preço = product['preço']
                
                return {'msg':f'{tipo} comprada por R${preço},00 pelo cliente {nome}!'}, 201
        return {'msg':'Precisa ser cliente para fazer uma compra'},404