import json
import unittest

from flask_jwt_extended.utils import create_access_token

from app import app
from src.models.user_model import UserModel

from connection import connection

class TestUserResource(unittest.TestCase):
    
    def setUp(self):
        connection.session.add(UserModel(name='John', password='pass', birth='09-08-2000', programming_languaje='javascript'))
        connection.session.add(UserModel(name='Juan', password='pass', birth='01-03-1987', programming_languaje='python'))
        self.__app = app.test_client()

        with self.__app.application.app_context():
            self.__access_token = create_access_token('testuser')

        self.__headers = {
            'Authorization': f'Bearer {self.__access_token}'
        }


    def tearDown(self):
        connection.session.query(UserModel).delete()
        connection.session.commit()

    def test_endpoint_users_get_all_users_returns_all_users_and_status_200(self):
        response = self.__app.get("/users", headers=self.__headers)
        response_json = json.loads(response.data.decode('utf-8'))

        self.assertEqual("John", response_json[0]['name'])
        self.assertEqual("09-08-2000", response_json[0]['birth'])
        self.assertEqual("javascript", response_json[0]['programming_languaje'])

        self.assertEqual("Juan", response_json[1]['name'])
        self.assertEqual("01-03-1987", response_json[1]['birth'])
        self.assertEqual("python", response_json[1]['programming_languaje'])

        self.assertEqual(200, response.status_code)

    def test_endopoint_users_post_new_user_returns_user_created_status_201(self):
        response = self.__app.post("/users", json={"name":"Lux", "password":"pass", "birth":"09-08-2000", "programming_languaje":"javascript"}, headers=self.__headers)
        response_json = json.loads(response.data.decode('utf-8'))

        self.assertEqual('Lux', response.json['name'])
        self.assertEqual("09-08-2000", response_json['birth'])
        self.assertEqual("javascript", response_json['programming_languaje'])
        self.assertEqual(201, response.status_code)

    def test_enpoint_users_put_new_name_returns_that_name_status_200(self):
        new_user = UserModel(name='Queso', password='pass', birth='09-08-2000', programming_languaje='javascript')
        connection.session.add(new_user)
        connection.session.commit()

        new_user_id = new_user.id
        user_updated = dict(id=new_user_id, name='Marcapaso')

        response = self.__app.put("/users", json=user_updated, headers=self.__headers)
        response_json = json.loads(response.data.decode('utf-8'))

        self.assertEqual('Marcapaso', response_json['name'])
        self.assertEqual(200, response.status_code)

    def test_delete_user_returns_status_204(self):
        new_user = UserModel(name='Quesito', password='pass', birth='09-08-2000', programming_languaje='javascript')
        connection.session.add(new_user)
        connection.session.commit()

        response = self.__app.delete("/users", json={"id": f"{new_user.id}"}, headers=self.__headers)

        self.assertEqual(204, response.status_code)
