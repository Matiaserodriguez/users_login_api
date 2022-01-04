import os

from flask import Flask
from flask_restx import Api
from flask_jwt_extended.jwt_manager import JWTManager

app = Flask(__name__)
api = Api(app, version='2.0', title='Users Login API', description='API for logging in users')

app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600
app.config['ERROR_INCLUDE_MESSAGE'] = False

jwt = JWTManager(app)