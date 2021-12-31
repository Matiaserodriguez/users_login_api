import os
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker

class Connection:
    def __init__(self, connectionstr):
        self.__engine = create_engine(connectionstr)
        Sesion = sessionmaker(bind = self.__engine)
        self.__sesion = Sesion()

    @property
    def engine(self):
        return self.__engine
    
    @property
    def sesion(self):
        return self.__sesion

    def __del__(self):
        self.__sesion.close()
        
connection = Connection(os.environ['DATABASE_ENV'])
