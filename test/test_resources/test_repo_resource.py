import json
import unittest

from flask_jwt_extended.utils import create_access_token

from app import app
from src.models.repo_model import RepoModel

from connection import connection

class TestRepoResource(unittest.TestCase):
    
    def setUp(self):
        connection.session.add(RepoModel(project_name='Cambalache', languaje='python'))
        connection.session.add(RepoModel(project_name='Cambalache2', languaje='javascript'))
        self.__app = app.test_client()

        with self.__app.application.app_context():
            self.__access_token = create_access_token('testuser')

        self.__headers = {
            'Authorization': f'Bearer {self.__access_token}'
        }

    def tearDown(self):
        connection.session.query(RepoModel).delete() 
        connection.session.commit()

    def test_endpoint_repos_get_all_repos_returns_all_repos_and_status_200(self):
        response = self.__app.get("/repos", headers=self.__headers)
        response_json = json.loads(response.data.decode('utf-8'))

        self.assertEqual("Cambalache", response_json[0]['project_name'])
        self.assertEqual("python", response_json[0]['languaje'])

        self.assertEqual("Cambalache2", response_json[1]['project_name'])
        self.assertEqual("javascript", response_json[1]['languaje'])

        self.assertEqual(200, response.status_code)

    def test_endopoint_repos_post_new_repo_returns_repo_created_status_201(self):
        response = self.__app.post("/repos", json={"project_name":"Lux", "languaje":"javascript"}, headers=self.__headers)
        response_json = json.loads(response.data.decode('utf-8'))

        self.assertEqual('Lux', response_json['project_name'])
        self.assertEqual("javascript", response_json['languaje'])


    def test_enpoint_repos_put_new_project_name_returns_that_project_name_status_200(self):
        new_repo = RepoModel(project_name='Queso', languaje='javascript')
        connection.session.add(new_repo)
        connection.session.commit()

        new_repo_id = new_repo.id
        # repo_updated = dict(id=new_repo_id, project_name='Marcapaso')

        response = self.__app.put("/repos", json={'id': f'{new_repo_id}', 'project_name': 'Marcapaso'}, headers=self.__headers)
        response_json = json.loads(response.data.decode('utf-8'))

        self.assertEqual('Marcapaso', response_json['project_name'])
        self.assertEqual(200, response.status_code)

    def test_delete_repo_returns_status_204(self):
        new_repo = RepoModel(project_name='Queso', languaje='javascript')
        connection.session.add(new_repo)
        connection.session.commit()

        response = self.__app.delete("/repos", json={"id": f"{new_repo.id}"}, headers=self.__headers)

        self.assertEqual(204, response.status_code)
