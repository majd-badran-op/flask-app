from typing import Generic, TypeVar, Type
from entities.baseclass import BaseEntity
E = TypeVar('E', bound='BaseEntity')


class BaseRepo(Generic[E]):
    students: list[E] = []

    def __init__(self, entity: Type[E]) -> None:
        self.entity = entity

    @classmethod
    def insert(cls, entity: E):
        BaseRepo.students.append(entity)
        return entity

    @classmethod
    def get_all(cls) -> list[E]:
        return BaseRepo.students

    @classmethod
    def get(cls, id: int) -> E | None:
        for s in BaseRepo.students:
            if s.id == id:
                return s
        return None

    @classmethod
    def update(cls, entity: E, id: int) -> bool:
        for i, s in BaseRepo.students:
            if s.id == id:
                BaseRepo.students[i] = entity
                return True
        return False

    @classmethod
    def delete(cls, id: int) -> bool:
        for i, s in BaseRepo.students:
            if s.id == id:
                BaseRepo.students.pop(i)
                return True
        return False
