import requests
from flask import Flask, request, json, jsonify
from flask_restful import Api, Resource
from . import api_bp
from service.AuthenService import *;
api = Api(api_bp)

def GetToken():
        result = GetAzureAuthentication();
        token = ""
        auth = {
            "grant_type":result[0][3],
            "client_id":result[0][0],
            "client_secret":result[0][1],
            "scope":result[0][2]
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post("https://login.microsoftonline.com/8ccfa3e1-88db-4035-9c29-23f65cf4026c/oauth2/v2.0/token", data=auth, headers=headers)
        data = response.json()
        if response.status_code == 200:
            token = data["access_token"]
        return token

class LearningAPI(Resource):
    def post(self):
        data = request.get_json()
        url = "http://n8n.og-19.online/webhook/send_email"
        response = requests.post(url, json=data)
        return "OK", 200
    
class Course(Resource):           
    def get(self):
        token = GetToken()
        listCourse = []
        try:
            url = "https://hi-iamngo.api.crm5.dynamics.com/api/data/v9.2/api_course_v1"
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
            data = request.get_json()
            response = requests.post(url, json=data, headers=headers)
            listCourse = response.json();
        except:
            listCourse = []
        return listCourse, 200

class getAuthen(Resource):
    def get(self):
        result = GetAzureAuthentication();
        auth = {
            "grant_type":result[0][3],
            "client_id":result[0][0],
            "client_secret":result[0][1],
            "scope":result[0][2]
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post("https://login.microsoftonline.com/8ccfa3e1-88db-4035-9c29-23f65cf4026c/oauth2/v2.0/token", data=auth, headers=headers)
        data = response.json()
        print(data["access_token"])
        return data, response.status_code
    
api.add_resource(LearningAPI, "/learning_v1")
api.add_resource(getAuthen, "/token_v1")
api.add_resource(Course, "/course_v1")