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
        auth = {
            "grant_type":"client_credentials",
            "client_id":"d705c688-e6d5-451f-b69f-7f27e5a39d43",
            "client_secret":"R4B8Q~LwQbEvqJnT2XpwrnV1f5sBGegLTplpWdbz",
            "scope":"https://hi-iamngo.crm5.dynamics.com/.default"
        }
        response = requests.post("https://login.microsoftonline.com/8ccfa3e1-88db-4035-9c29-23f65cf4026c/oauth2/v2.0/token", data=auth)
        return response, response.status_code
    
api.add_resource(LearningAPI, "/learning_v1")
api.add_resource(GetToken, "/token_v1")