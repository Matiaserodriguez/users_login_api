import unittest

from connection import connection
from src.models.user_model import UserModel
from src.services.user_service import user


class TestUserService(unittest.TestCase):

   def tearDown(self):
      connection.session.query(UserModel).delete()   

   def test_insert_user_returns_user_created(self):
      answer = user.insert("Queso", "password", "07/09/2008")

      self.assertEqual("Queso", answer.name)
      self.assertEqual("password", answer.password)
      self.assertEqual("07/09/2008", answer.birth)
      self.assertIsInstance(answer.id, int)