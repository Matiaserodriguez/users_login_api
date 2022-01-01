from sqlalchemy import Column, Integer, String, Enum

from . import Base
from src.services.tables_service import CreatesTable


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable = False, unique=True)
    password = Column(String(255), nullable=False)
    birth = Column(String(100), nullable=False)
    # programming_languajes = Column(Enum('python', 'JS', 'php', name="programming_languajes"), nullable=True)
    

user_table = CreatesTable(UserModel)
