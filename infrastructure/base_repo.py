from typing import Generic, TypeVar, Type, List
from domain.baseclass import BaseEntity
from database.con import get_connection
from sqlalchemy import Table, insert, select, update, delete
from sqlalchemy.engine import Result

E = TypeVar('E', bound=BaseEntity)


class BaseRepo(Generic[E]):
    def __init__(self, entity: Type[E], table: Table) -> None:
        self.entity = entity
        self.table = table

    def insert(self, entity: E) -> E:
        with get_connection() as session:
            data = {}
            for key, value in vars(entity).items():
                if key != 'id':
                    data[key] = value
            sql = insert(self.table).values(**data).returning(*self.table.columns)
            result: Result = session.execute(sql)
            session.commit()
            inserted_row = result.fetchone()
            if inserted_row:
                return self.entity(**inserted_row._mapping)
            return None

    def get_all(self) -> List[E]:
        with get_connection() as session:
            sql = select(self.table)
            result: Result = session.execute(sql)
            return [self.entity(**row._mapping) for row in result.fetchall()]

    def get(self, id: int) -> E | None:
        with get_connection() as session:
            sql = select(self.table).where(self.table.c.id == id)
            result: Result = session.execute(sql).fetchone()
            return self.entity(**result._mapping) if result else None

    def update(self, entity: E) -> bool:
        with get_connection() as session:
            data = {key: value for key, value in vars(entity).items() if key != 'id'}
            sql = update(self.table).where(self.table.c.id == entity.id).values(**data)
            result: Result = session.execute(sql)
            session.commit()
            return result.rowcount > 0

    def delete(self, id: int) -> bool:
        with get_connection() as session:
            sql = delete(self.table).where(self.table.c.id == id)
            result: Result = session.execute(sql)
            session.commit()
            return result.rowcount > 0
