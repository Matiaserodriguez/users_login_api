from datetime import datetime

from . import Base

from sqlalchemy import Column, Enum, String, DateTime, Integer


class LoginModel(Base):
    __tablename__ = 'login_report'
    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime(), default=datetime.now())
    type_of = Column(Enum, nullable=False)
    user_id = Column(String(255), nullable=False)
