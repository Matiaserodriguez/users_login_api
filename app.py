from src import app, api
from src.resources.user_resource import UsersResource


api.add_resource(UsersResource, '/users', endpoint='users_ep')