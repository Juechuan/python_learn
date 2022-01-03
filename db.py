"""DB Connect."""

from asyncpg import create_pool

import settings


class Database:

    def __init__(self) -> None:
        self.user = settings.POSTGRES_USER
        self.password = settings.POSTGRES_PASSWORD
        self.host = settings.POSTGRES_SERVER
        self.port = settings.POSTGRES_PORT
        self.database = settings.POSTGRES_DB

        self._pool = None
        self.con = None