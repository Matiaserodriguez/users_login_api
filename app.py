from src import app, api
from src.models.user_model import UserModel
from src.models.repo_model import RepoModel
from src.models.login_model import LoginModel
from src.resources.repo_resource import RepoResource
from src.resources.user_resource import UserLoginResource, UsersResource
from src.services.tables_service import CreatesTable
from src.services.user_service import user


api.add_resource(UsersResource, '/users', endpoint='users_ep')
api.add_resource(RepoResource, '/repos', endpoint='repos_ep')
api.add_resource(UserLoginResource, '/users/login', endpoint='login_ep')


user_table = CreatesTable(UserModel)
repo_table = CreatesTable(RepoModel)
login_table = CreatesTable(LoginModel)

login_table.create_table()
repo_table.create_table()
user_table.create_table()