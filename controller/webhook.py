from flask import Flask, request, json, jsonify
from flask_restful import Api, Resource
from . import api_bp
from authentication.Authen import *
api = Api(api_bp)

class Webhook(Resource):
    def post(self):
        data = request.get_json()
        print(data)
        return "OK", 200
    
    def get(self):
        hubChalange = request.args.get('hub.challenge')
        print(hubChalange)
        return hubChalange, 200

api.add_resource(Webhook, "/webhook")