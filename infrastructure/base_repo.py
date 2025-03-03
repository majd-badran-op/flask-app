from typing import Generic, TypeVar, Type
from domain.baseclass import BaseEntity
from database.con import get_connection
from sqlalchemy import Table, insert, select, update, delete

E = TypeVar("E", bound=BaseEntity)


class BaseRepo(Generic[E]):
    def __init__(self, entity: Type[E], table: Table) -> None:
        self.entity = entity
        self.table = table

    def insert(self, entity: E) -> E:
        with get_connection() as session:
            stmt = insert(self.table).values(
                id=entity.id,
                name=entity.name,
                age=entity.age,
                grade=getattr(entity, "grade", None)
            )
            session.execute(stmt)
            session.commit()
        return entity

    def get_all(self) -> list[E]:
        with get_connection() as session:
            stmt = select(self.table)
            result = session.execute(stmt)
            return [self.entity(**row._mapping) for row in result.fetchall()]

    def get(self, id: int) -> E | None:
        with get_connection() as session:
            stmt = select(self.table).where(self.table.c.id == id)
            result = session.execute(stmt).fetchone()
            return self.entity(**result._mapping) if result else None

    def update(self, entity: E, id: int) -> bool:
        with get_connection() as session:
            stmt = (
                update(self.table)
                .where(self.table.c.id == id)
                .values(name=entity.name, age=entity.age, grade=getattr(entity, "grade", None))
            )
            result = session.execute(stmt)
            session.commit()
            return result.rowcount > 0

    def delete(self, id: int) -> bool:
        with get_connection() as session:
            stmt = delete(self.table).where(self.table.c.id == id)
            result = session.execute(stmt)
            session.commit()
            return result.rowcount > 0
