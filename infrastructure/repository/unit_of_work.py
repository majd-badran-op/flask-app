from sqlalchemy.engine import Connection
from sqlalchemy.engine.base import Transaction
from typing import Optional, Type
from infrastructure.database.con import get_session
from types import TracebackType
from .student_repo import StudentRepo


class UnitOfWork:
    def __init__(self) -> None:
        self.connection: Optional[Connection] = None
        self.transaction: Optional[Transaction] = None
        self.repo: Optional[StudentRepo] = None

    def __enter__(self) -> 'UnitOfWork':
        self.connection = get_session()
        self.transaction = self.connection.begin()
        self.repo = StudentRepo()
        return self

    def commit(self) -> None:
        if self.transaction:
            try:
                self.transaction.commit()
            except Exception as e:
                self.rollback()
                raise e

    def rollback(self) -> None:
        if self.transaction:
            self.transaction.rollback()

    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException],
                 traceback: Optional[TracebackType]) -> None:
        if exc_type:
            self.rollback()
        if self.connection:
            self.connection.close()
