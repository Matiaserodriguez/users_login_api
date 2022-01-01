from src.models.user_model import UserModel
from .connect_service import ConnectionService
from .commit_after_service import commit_after


class UserService(ConnectionService):

    @commit_after
    def insert(self, name, password, birth):
        new_user = UserModel(name=name, password=password, birth=birth)
        self._session.add(new_user)

        return new_user

user = UserService()
