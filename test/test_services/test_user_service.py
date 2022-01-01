import unittest

from connection import connection
from src.models.user_model import UserModel
from src.services.user_service import user


class TestUserService(unittest.TestCase):

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