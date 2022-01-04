from src.models.login_model import LoginModel
from src.models.user_model import UserModel
from .connect_service import ConnectionService
from .commit_after_service import commit_after
from connection import connection


class LoginService(ConnectionService):

    @commit_after
    def insert(self, type_of, name):
        user = self._session.query(UserModel).filter(UserModel.name == name).first()
        new_login = LoginModel(type_of=type_of, user_id=user.id)

        self._session.add(new_login)

        return new_login

login_serv = LoginService()