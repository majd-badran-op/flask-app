from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
from dotenv import load_dotenv
import os

load_dotenv()
engine = create_engine(os.getenv('DATABASE_URL'))


class UnitOfWork:
    def __init__(self):
        self.connection: Connection = None
        self.session = None

    def __enter__(self):
        self.connection = engine.connect()
        self.session = self.connection.begin()
        return self

    def commit(self):
        try:
            self.session.commit()
        except Exception as e:
            self.rollback()
            raise e

    def rollback(self):
        if self.session:
            self.session.rollback()

    def execute(self, sql):
        return self.connection.execute(sql)

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.rollback()
        self.connection.close()
