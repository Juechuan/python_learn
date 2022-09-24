"""Main.py for fastapi."""
from fastapi import FastAPI
from loguru import logger
# from db_session import db_instance

app = FastAPI()
logger.add('runtime.log', format="{time} {level} {message}")
logger.info('Init fastapi app.')


@app.get('/')
async def root():
    """Fastapi Root route."""
    logger.info('Request from root.')
    return 'message: "Hello world!"'


@logger.trace
@app.get('/sql')
async def sql_test():
    """Fastapi Sql test."""
    logger.info('Request from sql.')
    result = await db_instance.fetch_rows("select * from public.py_user")
    print(result)
    return 'sql: "Hello sql."'
