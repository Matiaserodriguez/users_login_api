from datetime import date

from . import Base

from sqlalchemy import Column, Integer, String, Enum, Date


class RepoModel(Base):
    __tablename__ = 'repositories'
    id = Column(Integer, primary_key=True)
    proyect_name = Column(String(255), nullable=False)
    languaje = Column(Enum, nullable=False)
    creation_date = Column(Date(), default=date.now(), nullable=False)
    description = Column(String)
