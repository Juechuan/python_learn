"""Main.py for fastapi."""
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    """Fastapi Root route."""
    return 'message: "Hello world!"'
