from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import locations as loc
from users import users_api

app = Flask(__name__)
app.register_blueprint(users_api, url_prefix='/users')

api = Api(app)

# api.add_resource(u.Users, '/users')
# api.add_resource(loc.Locations, '/locations')


if __name__ == '__main__':
    app.run() # runs our Flask app