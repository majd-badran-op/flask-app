from sqlalchemy import create_engine
from sqlalchemy.engine import Connection

DATABASE_URL = 'postgresql://majd:078818@localhost:5432/test'

engine = create_engine(DATABASE_URL)


def get_connection() -> Connection:
    return engine.connect()
