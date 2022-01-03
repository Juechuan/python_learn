"""DB Connect."""

from asyncpg import create_pool

import settings
from loguru import logger


class Database:
    def __init__(self) -> None:
        self.user = settings.POSTGRES_USER
        self.password = settings.POSTGRES_PASSWORD
        self.host = settings.POSTGRES_SERVER
        self.port = settings.POSTGRES_PORT
        self.database = settings.POSTGRES_DB

        self._pool = None

    async def connect(self):
        if not self._pool:
            try:
                self._pool = await create_pool(
                    min_size=1,
                    max_size=10,
                    command_timeout=60,
                    host=self.host,
                    port=self.port,
                    user=self.user,
                    password=self.password,
                    database=self.database,
                )
            except Exception as e:
                print(e)

    @logger.catch
    async def fetch_rows(self, query: str):
        if not self._pool:
            await self.connect()
        else:
            con = await self._pool.acquire()
            try:
                result = await con.fetch(query)
                return result
            except Exception as e:
                print(e)
            finally:
                await self._pool.release(con)
