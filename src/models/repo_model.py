from datetime import date

from sqlalchemy import Column, Integer, String, Enum, DateTime

from src.models.user_model import ProgrammingLanguajes

from . import Base


class RepoModel(Base):
    __tablename__ = 'repositories'
    id = Column(Integer, primary_key=True)
    project_name = Column(String(255), nullable=False)
    languaje = Column(Enum(ProgrammingLanguajes), nullable=False)
    creation_date = Column(DateTime(), default=date.today(), nullable=False)
    description = Column(String)
