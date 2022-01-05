from flask_restx import Resource, fields
from flask_jwt_extended import create_access_token, jwt_required

from src.models.user_model import ProgrammingLanguajes
from ..services import user, login_serv
from src import api


user_model = api.model('Users', {
    'id': fields.Integer,
    'name': fields.String(attribute='name'),
    'birth': fields.String(attribute='birth'),
    'programming_languaje': fields.String(
        attribute='programming_languaje.name', 
        default=None, 
        description='Programming Languajes only accepts python, javascript, php'
    )
})

login_model = api.model('User Login', {
    'name': fields.String(attribute='name'),
    'password': fields.String(attribute='password')
})

class UsersResource(Resource):
    @api.marshal_with(user_model, code=200)
    @jwt_required()
    def get(self):
        try:
            answer = user.obtain_all()

        except:
            return {'400': 'Bad Request'}, 400
        
        return answer, 200

    @api.marshal_with(user_model, code=201)
    def post(self):
        for lenguaje in list(ProgrammingLanguajes):
            if api.payload['programming_languaje'].lower() in str(lenguaje):
                answer = user.insert(api.payload['name'], api.payload['password'], api.payload['birth'], api.payload['programming_languaje'].lower())
                login_serv.insert('sign-up', api.payload['name'])
                return answer, 201
        
        answer = user.insert(api.payload['name'], api.payload['password'], api.payload['birth'])
        login_serv.insert('sign-up', api.payload['name'])
        return answer, 201

    @api.marshal_with(user_model, code=200)
    @jwt_required()
    def put(self):
        
        value = list(api.payload.keys())[1:][0]
        kw = {value: api.payload[value]}
        
        answer = user.update(api.payload['id'], **kw)

        return answer, 200

    @jwt_required()
    def delete(self):
        user.delete_one(api.payload['id'])
        return "", 204

class UserLoginResource(Resource):
    @api.expect(login_model)
    def post(self):

        if user.login(api.payload['name'], api.payload['password']):
            access_token = create_access_token(identity=api.payload['name'])
            login_serv.insert('login', api.payload['name'])
            return {'token': access_token}, 201

        else:
            return {'msg': 'Username and/or password is incorrect'}, 401
            