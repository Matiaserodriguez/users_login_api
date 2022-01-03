from flask_restx import Resource, fields

from src.models.user_model import ProgrammingLanguajes
from ..services import user
from src import api


user_model = api.model('Users', {
    'id': fields.Integer,
    'name': fields.String(attribute='name'),
    'birth': fields.String(attribute='birth'),
    'programming_languaje': fields.String(attribute='programming_languaje.name', default=None)
})

class UsersResource(Resource):
    @api.marshal_with(user_model, code=200)
    def get(self):
        try:
            answer = user.obtain_all()

        except:
            return {'Error 400': 'Bad Request'}, 400
        
        return answer, 200

    @api.marshal_with(user_model, code=201)
    def post(self):
        for lenguaje in list(ProgrammingLanguajes):
            if api.payload['programming_languaje'].lower() in str(lenguaje):
                answer = user.insert(api.payload['name'], api.payload['password'], api.payload['birth'], api.payload['programming_languaje'].lower())
                return answer, 201
        
        answer = user.insert(api.payload['name'], api.payload['password'], api.payload['birth'])
        return answer, 201

    @api.marshal_with(user_model, code=200)
    def put(self):

        value = list(api.payload.keys())[1:][0]
        if value == 'name':
            answer = user.update(api.payload['id'], name=api.payload[value])
        elif value == 'birth':
            answer = user.update(api.payload['id'], birth=api.payload[value])
        elif value == 'password':
            answer = user.update(api.payload['id'], password=api.payload[value])
        elif value == 'programming_languaje':
            if value == None:
                return {400: 'Not recognized or bad programming languaje'}, 400
            answer = user.update(api.payload['id'], programming_languaje=api.payload[value])

        return answer, 200

    def delete(self):
        user.delete_one(api.payload['id'])
        return "", 204
