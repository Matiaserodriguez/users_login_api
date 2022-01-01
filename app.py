from src import app, api
from src.models.user_model import UserModel
from src.models.repo_model import RepoModel
from src.models.login_model import LoginModel
from src.resources.user_resource import UsersResource
from src.services.tables_service import CreatesTable
from src.services.user_service import user


api.add_resource(UsersResource, '/users', endpoint='users_ep')

user_table = CreatesTable(UserModel)
repo_table = CreatesTable(RepoModel)
login_table = CreatesTable(LoginModel)

login_table.create_table()
repo_table.create_table()
user_table.create_table()

# user.insert("Jaimito", "password", "07/09/2008")

# if __name__ == '__main__':
#     app.run(debug=True)