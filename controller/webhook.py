import requests
from flask import Flask, request, json, jsonify
from flask_restful import Api, Resource
from . import api_bp
from authentication.Authen import *
api = Api(api_bp)

class Webhook(Resource):
    def post(self):
        data = request.get_json()
        print(data)
        url = "http://n8n.og-19.online/webhook/97c84d0e-b45f-4b82-824b-32b182f3f91c"
        response = requests.post(url, json=data)
        return "OK", 200
    
    def get(self):
        hubChalange = request.args.get('hub.challenge')
        print(hubChalange)
        return int(hubChalange), 200

api.add_resource(Webhook, "/webhook")