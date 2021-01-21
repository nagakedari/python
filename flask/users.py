from flask_restful import Resource, reqparse
from flask import request, jsonify
import pandas as pd
import os
import re
from flask import Blueprint

users_api = Blueprint('users_api', __name__) # Blueprints helps splitting the flask api in to multiple files

class Users(Resource): # Flask needs to know that this class is an endpoint for our API, and so we pass Resource in with the class definition
    #pass # pass statement is to avoid empty code error. We will get that error in loop, conditions, class definitions..etc
    
    def get(self):
        data = pd.read_csv(os.path.join(os.curdir, 'users.csv'))
        data = data.to_dict()
        return {'data': data}, 200
    
    def post(self, payload):
        data = pd.read_csv(os.path.join(os.curdir, 'users.csv'))
        if payload['userId'] in list(data['userId']):
            return {
                'message': f"'{payload['userId']}' aleady exists"
            }, 401
        data = data.append(payload, ignore_index=True)
        data.to_csv(os.path.join(os.curdir, 'users.csv'), index=False)
        return {'data': data.to_dict()}, 200
    
    def findWithParameters(self, params):
        data = pd.read_csv(os.path.join(os.curdir, 'users.csv'))
        data_positions_that_match_criteria = pd.DataFrame([data[key]== val for key, val in params.items()]).T.all(axis=1)
        filtered_data = data[data_positions_that_match_criteria]
        return {} if data_positions_that_match_criteria.empty else {'data' : filtered_data.to_dict() }, 200 
        
userObj = Users()
@users_api.route("/", methods=['GET'])
def get():
    return userObj.get()

@users_api.route("/", methods=['POST'])
def post():
    payload = request.json
    return userObj.post(payload)

@users_api.route("/filter", methods=['GET'])
def findByCriteria():
    parser = reqparse.RequestParser()
    parser.add_argument('userId')  # add args
    parser.add_argument('city')

    params = parser.parse_args()
    return userObj.findWithParameters(params)

