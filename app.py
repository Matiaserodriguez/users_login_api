from src import app, api
from src.models.login_model import login_table
from src.models.repo_model import repo_table
from src.models.user_model import user_table
from src.resources.user_resource import UsersResource
from src.services.user_service import user


api.add_resource(UsersResource, '/users', endpoint='users_ep')

login_table.create_table()
repo_table.create_table()
user_table.create_table()

# user.insert("Jaimito", "password", "07/09/2008")

# if __name__ == '__main__':
#     app.run(debug=True)