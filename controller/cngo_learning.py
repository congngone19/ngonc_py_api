import requests
from flask import Flask, request, json, jsonify
from flask_restful import Api, Resource
from . import api_bp
api = Api(api_bp)

class LearningAPI(Resource):
    def post(self):
        data = request.get_json()
        url = "http://n8n.og-19.online/webhook/send_email"
        response = requests.post(url, json=data)
        return "OK", 200
    
class GetToken(Resource):
    def get(self):
        url = request.args.get('url')
        auth = {
            
        }
        response = requests.post(url, data=auth)
        return response, response.status_code
    
api.add_resource(LearningAPI, "/learning_v1")
api.add_resource(GetToken, "/token_v1")