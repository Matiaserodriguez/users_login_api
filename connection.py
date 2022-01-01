import os
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker

class Connection:
    def __init__(self, connectionstr):
        self.__engine = create_engine(connectionstr)
        Session = sessionmaker(bind = self.__engine)
        self.__session = Session()

    @property
    def engine(self):
        return self.__engine
    
    @property
    def session(self):
        return self.__session

    def __del__(self):
        self.__session.close()
        
connection = Connection("postgresql://qmnqluroxinfta:2025938ff1f39fef4a03ef2cecd8016001905cb9f84c3772fec4e4b22487ae4f@ec2-52-70-205-234.compute-1.amazonaws.com:5432/dfmjq7ss6pvs8r")
