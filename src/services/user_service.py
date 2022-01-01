from src.models.user_model import ProgrammingLanguajes, UserModel
from .connect_service import ConnectionService
from .commit_after_service import commit_after


class UserService(ConnectionService):

    def obtain_all(self):
        return self._session.query(UserModel).all()

    @commit_after
    def insert(self, name, password, birth, languaje):
        new_user = UserModel(name=name, password=password, birth=birth, programming_languaje=languaje)
        self._session.add(new_user)

        return new_user

user = UserService()
