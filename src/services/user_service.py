from sqlalchemy.exc import IntegrityError
from src.models.user_model import ProgrammingLanguajes, UserModel
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
            if key == 'name':
                user_to_update.name = value
            elif key == 'password':
                user_to_update.password = value
            elif key == 'birth':
                user_to_update.birth = value
            elif key == 'programming_languaje':
                for i in list(ProgrammingLanguajes):
                    if value.lower() in str(i):
                        user_to_update.programming_languaje = value.lower()
                        return user_to_update

                user_to_update.programming_languaje = None

            return user_to_update

    @commit_after
    def delete_one(self, _id):
        user_to_delete = self.obtain_one(_id)
        self._session.delete(user_to_delete)


user = UserService()
