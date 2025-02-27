from typing import Generic, TypeVar, Type, Any
from entities.baseclass import BaseEntity
E = TypeVar('E', bound='BaseEntity')


class BaseRepo(Generic[E]):
    students: list[E] = []

    def __init__(self, entity: Type[E]) -> None:
        self.entity = entity

    @classmethod
    def insert(cls, entity: E) -> E:
        cls.students.append(entity)
        return entity

    @classmethod
    def get_all(cls) -> list[E]:
        return cls.students

    @classmethod
    def get(cls, id: int) -> E | None | Any:
        for s in cls.students:
            if s.id == id:
                return s
        return None

    @classmethod
    def update(cls, entity: E, id: int) -> bool:
        for i, s in enumerate(cls.students):
            if s.id == id:
                cls.students[i] = entity
                return True
        return False

    @classmethod
    def delete(cls, id: int) -> bool:
        for i, s in enumerate(cls.students):
            if s.id == id:
                cls.students.pop(i)
                return True
        return False
