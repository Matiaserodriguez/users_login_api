import enum
from sqlalchemy import Column, Integer, String, Enum

from . import Base

class ProgrammingLanguajes(enum.Enum):
    python = 1
    javascript = 2
    php = 3

class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable = False, unique=True)
    password = Column(String(255), nullable=False)
    birth = Column(String(100), nullable=False)
    programming_languaje = Column(Enum(ProgrammingLanguajes), nullable=True)
