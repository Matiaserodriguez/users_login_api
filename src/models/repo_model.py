from datetime import date

from sqlalchemy.sql.sqltypes import DateTime

from . import Base

from sqlalchemy import Column, Integer, String, Enum, Date
from src.services.tables_service import CreatesTable


class RepoModel(Base):
    __tablename__ = 'repositories'
    id = Column(Integer, primary_key=True)
    proyect_name = Column(String(255), nullable=False)
    languaje = Column(Enum(name="kinds_of_languajes"), nullable=False)
    creation_date = Column(DateTime(), default=date, nullable=False)
    description = Column(String)

repo_table = CreatesTable(RepoModel)
