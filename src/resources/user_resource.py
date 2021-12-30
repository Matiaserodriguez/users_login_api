from flask_restx import Resource

class UsersResource(Resource):
    def get(self):
        return 'Hello, I\'m the user\'s resource!'
        