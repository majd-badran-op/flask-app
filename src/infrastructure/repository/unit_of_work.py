from sqlalchemy.orm import Session
from infrastructure.repository.base_repo import BaseRepo
from typing import Optional, Type, Any
from infrastructure.database.con import get_session
from types import TracebackType


class DatabaseException(Exception):
    pass


class UnitOfWork:
    def __init__(self, repo_class: BaseRepo[Any]) -> None:
        self.session: Session
        self.repo = repo_class

    def __enter__(self) -> 'UnitOfWork':
        self.session = get_session()
        self.transaction = self.session.begin()
        return self

    def commit(self) -> None:
        if self.session:
            try:
                self.session.commit()
            except Exception as e:
                self.rollback()
                raise e

    def rollback(self) -> None:
        if self.session:
            self.session.rollback()

    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException],
                 traceback: Optional[TracebackType]) -> None:
        if exc_type:
            self.rollback()
        if self.session:
            self.commit()
            self.session.close()
