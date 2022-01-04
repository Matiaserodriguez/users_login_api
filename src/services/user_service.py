from sqlalchemy.sql.elements import and_
from src.models.user_model import UserModel
from .connect_service import ConnectionService
from .commit_after_service import commit_after
from connection import connection


class UserService(ConnectionService):

    def obtain_one(self, _id):
        return self._session.query(UserModel).filter(UserModel.id == _id).first()

    def obtain_all(self):
        return self._session.query(UserModel).all()

    @commit_after
    def insert(self, name, password, birth, languaje=None):
        new_user = UserModel(name=name, password=password, birth=birth, programming_languaje=languaje)
        self._session.add(new_user)

        return new_user

    @commit_after
    def update(self, _id, **kwargs):
        user_to_update = self.obtain_one(_id)

        for key, value in kwargs.items():
            setattr(user_to_update, key, value)

        return user_to_update

    @commit_after
    def delete_one(self, _id):
        user_to_delete = self.obtain_one(_id)
        self._session.delete(user_to_delete)

    def login(self, name, password):

        user = self._session.query(UserModel).filter(and_(UserModel.name == name, UserModel.password == password)).first()

        if user == None:
            return False
        
        return user

user = UserService()
