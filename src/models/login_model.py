from datetime import datetime
from sqlalchemy import Column, Enum, String, DateTime, Integer

from . import Base


class LoginModel(Base):
    __tablename__ = 'login_report'
    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime(), default=datetime.now())
    type_of = Column(Enum('login', 'sign-up', name='type_login'), nullable=False)
    user_id = Column(String(255), nullable=False)
