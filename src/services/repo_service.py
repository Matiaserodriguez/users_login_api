from datetime import date
from src.models.repo_model import RepoModel
from .connect_service import ConnectionService
from .commit_after_service import commit_after
from connection import connection


class RepoService(ConnectionService):

    def obtain_one(self, _id):
        return self._session.query(RepoModel).filter(RepoModel.id == _id).first()

    def obtain_all(self):
        return self._session.query(RepoModel).all()

    @commit_after
    def insert(self, project_name, languaje, description=None):
        new_user = RepoModel(project_name=project_name, languaje=languaje, description=description)
        self._session.add(new_user)

        return new_user

    @commit_after
    def update(self, _id, **kwargs):
        repo_to_update = self.obtain_one(_id)

        for key, value in kwargs.items():
            setattr(repo_to_update, key, value)

        return repo_to_update

    @commit_after
    def delete_one(self, _id):
        repo_to_delete = self.obtain_one(_id)
        self._session.delete(repo_to_delete)


repo = RepoService()