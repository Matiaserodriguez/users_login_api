from connection import connection
from .commit_after_service import commit_after


class CreatesTable:
    def __init__(self, table):
        self.__table = table

    @commit_after
    def create_table(self):
        self.__table.__table__.create(bind=connection.engine, checkfirst=True)
