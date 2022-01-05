from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

from .user_model import UserModel
from .repo_model import RepoModel
from .login_model import LoginModel
