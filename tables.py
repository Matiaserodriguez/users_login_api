from connection import connection


class CreatesTable:
    def __init__(self, table):
        self.__table = table

    def create_table(self):
        self.__table.__table__.create(bind=connection.engine, checkfirst=True)
        connection.sesion.commit()