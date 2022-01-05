import os
from .config import user, password, host, database
# import tempfile

path_database = f'postgresql://{user}:{password}@{host}/{database}'
os.environ['DATABASE_ENV'] = path_database
os.environ['JWT_SECRET_KEY'] = "clave secreta"
if os.path.exists(path_database):
    os.remove(path_database)

from src.models import Base
from connection import connection

Base.metadata.create_all(connection.engine)