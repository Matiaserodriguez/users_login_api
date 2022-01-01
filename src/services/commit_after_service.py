import functools
from connection import connection
from sqlalchemy.exc import IntegrityError

def commit_after(data_function):
    @functools.wraps(data_function)
    def wrapper(*args):
        try:
            new_object = data_function(*args)
            connection.session.commit()
        except IntegrityError:
            connection.session.rollback()
            raise IntegrityError
        else:
            return new_object
    return wrapper