from sqlalchemy.engine import Connection, Result
from sqlalchemy.sql import Executable
from sqlalchemy.engine.base import Transaction
from typing import Optional, Type
from dotenv import load_dotenv
from types import TracebackType
import os
from sqlalchemy import create_engine

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL') or ''
engine = create_engine(DATABASE_URL)


class UnitOfWork:
    def __init__(self) -> None:
        self.connection: Optional[Connection] = None
        self.transaction: Optional[Transaction] = None

    def __enter__(self) -> 'UnitOfWork':
        self.connection = engine.connect()
        self.transaction = self.connection.begin()
        return self

    def commit(self) -> None:
        if self.transaction:
            try:
                self.transaction.commit()
            except Exception:
                self.rollback()
                raise

    def rollback(self) -> None:
        if self.transaction:
            self.transaction.rollback()

    def execute(self, sql: Executable) -> Result:
        if self.connection:
            return self.connection.execute(sql)
        raise RuntimeError('Database connection is not established.')

    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException],
                 traceback: Optional[TracebackType]) -> None:
        if exc_type:
            self.rollback()
        if self.connection:
            self.connection.close()
