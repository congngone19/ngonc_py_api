import requests
from flask import Flask, request, json, jsonify
from flask_restful import Api, Resource
from . import api_bp
from service.AuthenService import *;
api = Api(api_bp)

class LearningAPI(Resource):
    def post(self):
        data = request.get_json()
        url = "http://n8n.og-19.online/webhook/send_email"
        response = requests.post(url, json=data)
        return "OK", 200
    
class getAuthen(Resource):
    def get(self):
        result = GetAzureAuthentication();
        auth = {
            "grant_type":result[0][3],
            "client_id":result[0][0],
            "client_secret":result[0][1],
            "scope":result[0][2]
        }
        response = requests.post("", data=auth)
        return response, response.status_code
    
api.add_resource(LearningAPI, "/learning_v1")
api.add_resource(getAuthen, "/token_v1")