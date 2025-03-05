from typing import Generic, TypeVar, Type, List, Optional, Any
from domain.base_class import BaseEntity
from sqlalchemy import Table, insert, select, update, delete
from sqlalchemy.engine import Result, Connection

E = TypeVar('E', bound=BaseEntity)


class BaseRepo(Generic[E]):
    def __init__(self, entity: Type[E], table: Table, session: Connection) -> None:
        self.entity = entity
        self.table = table
        self.con = session

    def insert(self, entity: E) -> Optional[E]:
        data = {key: value for key, value in vars(entity).items() if key != 'id'}
        sql = insert(self.table).values(**data).returning(*self.table.columns)
        result = self.con.execute(sql)
        inserted_row = result.fetchone()
        return self.entity(**inserted_row._mapping) if inserted_row else None

    def get_all(self) -> List[E]:
        sql = select(self.table)
        result = self.con.execute(sql)
        entities = [self.entity(**row._mapping) for row in result.fetchall()]
        return entities

    def get(self, id: int) -> Optional[E]:
        sql = select(self.table).where(self.table.c.id == id)
        result = self.con.execute(sql).fetchone()
        return self.entity(**result._mapping) if result else None

    def update(self, entity: E, id: int) -> bool:
        data = {key: value for key, value in vars(entity).items() if key != 'id'}
        sql = update(self.table).where(self.table.c.id == id).values(**data)
        result: Result[Any] = self.con.execute(sql)
        return result.rowcount > 0

    def delete(self, id: int) -> bool:
        sql = delete(self.table).where(self.table.c.id == id)
        result: Result[Any] = self.con.execute(sql)
        return result.rowcount > 0
