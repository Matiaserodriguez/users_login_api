import unittest

from connection import connection
from src.models.user_model import UserModel
from src.services.user_service import user


class TestUserService(unittest.TestCase):

    def setUp(self):
        connection.session.add(UserModel(name='John', password='pass', birth='09-08-2000', programming_languaje='javascript'))
        connection.session.add(UserModel(name='Juan', password='pass', birth='01-03-1987', programming_languaje='python'))

    def tearDown(self):
        connection.session.query(UserModel).delete() 
        connection.session.commit()

    def test_insert_user_returns_user_created(self):
        answer = user.insert("Pasta", "password", "07/09/2008", 'python')

        self.assertEqual("Pasta", answer.name)
        self.assertEqual("password", answer.password)
        self.assertEqual("07/09/2008", answer.birth)
        self.assertEqual("python", answer.programming_languaje.name)
        self.assertIsInstance(answer.id, int)

    def test_query_all_users_and_get_values(self):
        answer = user.obtain_all()

        self.assertEqual('John', answer[0].name)
        self.assertEqual('pass', answer[0].password)
        self.assertEqual('09-08-2000', answer[0].birth)
        self.assertEqual('javascript', answer[0].programming_languaje.name)

        self.assertEqual('Juan', answer[1].name)
        self.assertEqual('pass', answer[1].password)
        self.assertEqual('01-03-1987', answer[1].birth)
        self.assertEqual('python', answer[1].programming_languaje.name)
