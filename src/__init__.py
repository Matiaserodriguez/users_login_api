from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(app, version='2.0', title='Users Login API', description='API for logging in users')
