import os
# import tempfile

# path_database = f'{tempfile.gettempdir()}/login_users_api.db'
# os.environ['DATABASE_ENV'] = f'SQLITE:///{path_database}'
# if os.path.exists(path_database):
#     os.remove(path_database)

# from src.models import Base
from connection import connection

# Base.metadata.create_all(connection.engine)