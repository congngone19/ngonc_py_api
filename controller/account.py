from service.AccountService import *
from flask import Flask, request, json, jsonify
from flask_restful import Api, Resource
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from . import api_bp
from authentication.Authen import *
api = Api(api_bp)

class AccountController(Resource):
    def post(self):
        data = request.get_json()
        username = data["username"]
        pwd = data["pwd"]
        account = GetAccountByUsernamePassword(username, pwd)
        if len(account) == 1:
            access_token = create_access_token(identity=data["username"])
            return {"access_token": access_token}, 200
        else:
            return "Failed", 403
        
    @jwt_required()
    def get(self):
        account = GetAccountByUsername("ngonc")
        return account, 200

class AccountAuthen(Resource):
    def post(self):
        data = request.get_json()
        username = data["username"]
        pwd = data["pwd"]
        print(data)
        user = authenticate_user(username, pwd)
        if user:
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(
                data={"sub": user[0]}, expires_delta=access_token_expires
            )
            print(access_token)
            return {"access_token":access_token, "token_type":"bearer"}, 200
        else:
            return "Failed", 403

api.add_resource(AccountController, "/account")
api.add_resource(AccountAuthen, "/authen")