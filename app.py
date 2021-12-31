from src import app, api
from src.models.login_model import login_table
from src.models.repo_model import repo_table
from src.models.user_model import user_table
from src.resources.user_resource import UsersResource


api.add_resource(UsersResource, '/users', endpoint='users_ep')

login_table.create_table()
repo_table.create_table()
user_table.create_table()

# if __name__ == '__main__':
#     app.run(debug=True)