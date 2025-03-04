from typing import Generic, TypeVar, Type, List, Optional
from domain.base_class import BaseEntity
from infrastructure.repository.unit_of_work import UnitOfWork
from sqlalchemy import Table, insert, select, update, delete
from sqlalchemy.engine import Result, Row

E = TypeVar('E', bound=BaseEntity)


class BaseRepo(Generic[E]):
    def __init__(self, entity: Type[E], table: Table) -> None:
        self.entity = entity
        self.table = table

    def insert(self, entity: E) -> Optional[E]:
        with UnitOfWork() as session:
            data = {key: value for key, value in vars(entity).items() if key != 'id'}
            sql = insert(self.table).values(**data).returning(*self.table.columns)
            result: Result = session.execute(sql)  # Store the result
            session.commit()
            inserted_row = result.fetchone()
            return self.entity(**inserted_row._mapping) if inserted_row else None

    def get_all(self) -> List[E]:
        with UnitOfWork() as session:
            sql = select(self.table)
            result: Result = session.execute(sql)
            return [self.entity(**row._mapping) for row in result.fetchall()]

    def get(self, id: int) -> Optional[E]:
        with UnitOfWork() as session:
            sql = select(self.table).where(self.table.c.id == id)
            result: Row = session.execute(sql).fetchone()
            return self.entity(**result._mapping) if result else None

    def update(self, entity: E, id: int) -> bool:
        with UnitOfWork() as session:
            data = {key: value for key, value in vars(entity).items() if key != 'id'}
            sql = update(self.table).where(self.table.c.id == id).values(**data)
            result: Result = session.execute(sql)
            session.commit()
            return result.rowcount > 0

    def delete(self, id: int) -> bool:
        with UnitOfWork() as session:
            sql = delete(self.table).where(self.table.c.id == id)
            result: Result = session.execute(sql)
            session.commit()
            return result.rowcount > 0
