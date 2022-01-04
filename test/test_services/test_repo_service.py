import unittest

from connection import connection
from src.models.repo_model import RepoModel
from src.services.repo_service import repo


class TestRepoService(unittest.TestCase):

    def setUp(self):
        connection.session.add(RepoModel(project_name='Cambalache', languaje='python'))

    def tearDown(self):
        connection.session.query(RepoModel).delete() 
        connection.session.commit()

    def test_insert_repo_returns_repo_created(self):
        answer = repo.insert("Cambalache", "python", 'this is the description')

        self.assertEqual("Cambalache", answer.project_name)
        self.assertEqual("python", answer.languaje.name)
        self.assertEqual('this is the description', answer.description)

    def test_obtain_repo_recently_created_returns_that_repo_values(self):
        repo1 = repo.insert("Pizza", "javascript", 'description')
        answer = repo.obtain_one(repo1.id)

        self.assertEqual('Pizza', answer.project_name)
        self.assertEqual('javascript', answer.languaje.name)
        self.assertEqual('description', answer.description)

    def test_update_repo_already_created_returns_repo_with_changed_values(self):
        repo1 = repo.insert("Pizza", "javascript", 'description')
        repo1_updated = repo.update(repo1.id, project_name='Estofado', languaje='python', description='new_description')

        self.assertEqual('Estofado', repo1_updated.project_name)
        self.assertEqual('python', repo1_updated.languaje.name)
        self.assertEqual('new_description', repo1_updated.description)

    def test_delete_one_repo_returns_none_as_answer(self):
        repo1 = repo.insert("Pizza", "javascript", 'description')
        repo.delete_one(repo1.id)

        answer = repo.obtain_one(repo1.id)

        self.assertEqual(None, answer)
    