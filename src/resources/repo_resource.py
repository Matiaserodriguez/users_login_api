from flask_jwt_extended import jwt_required
from flask_restx import Resource, fields

from src.models.user_model import ProgrammingLanguajes
from ..services import repo
from src import api

repo_model = api.model('Repositories', {
    'id': fields.Integer(readonly=True, description='Repo ID, not necessary for HTTP requests'),
    'project_name': fields.String(attribute='project_name'),
    'languaje': fields.String(attribute='languaje.name', description='"languaje" only accepts python, javascript, php, c, sql, swift, ruby'),
    'creation_date': fields.Date(attribute='creation_date'),
    'description': fields.String(attribute='description', default=None, description='[optional]')
})


class RepoResource(Resource):
    @api.marshal_with(repo_model, code=200)
    @jwt_required()
    def get(self):
        answer = repo.obtain_all()

        return answer, 200

    @api.marshal_with(repo_model, code=201)
    @jwt_required()
    def post(self):
        try:
            for lenguaje in list(ProgrammingLanguajes):
                if api.payload['languaje'].lower() == str(lenguaje.name):
                    try:
                        answer = repo.insert(api.payload['project_name'], api.payload['languaje'].lower(), api.payload['description'])
                        return answer, 201
                    except KeyError:
                        answer2 = repo.insert(api.payload['project_name'], api.payload['languaje'].lower())
                        return answer2, 201

        except KeyError:
            return {400: 'Bad Request'}, 400
        

    @api.marshal_with(repo_model, code=200)
    @jwt_required()
    def put(self):
        value = list(api.payload.keys())[1:][0]
        kw = {value: api.payload[value]}
        
        answer = repo.update(api.payload['id'], **kw)

        return answer, 200

    @api.doc(params={'id': 'Integer ID'})
    @jwt_required()
    def delete(self):
        repo.delete_one(api.payload['id'])
        return "", 204
