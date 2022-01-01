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
        
connection = Connection(os.environ['DATABASE_ENV'])
