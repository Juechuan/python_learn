"""Main.py for fastapi."""
from fastapi import FastAPI
from db_session import db_instance

app = FastAPI()


@app.get('/')
async def root():
    """Fastapi Root route."""
    return 'message: "Hello world!"'


@app.get('/sql')
async def sql_test():
    """Fastapi Sql test."""
    result = await db_instance.fetch_rows("select * from public.py_user")
    print(result)
    return 'sql: "Hello sql."'
