from . import connection
from abc import ABC


class ConnectionService(ABC):
    _session = connection.session