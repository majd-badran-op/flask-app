from typing import Generic, TypeVar, Type
from entities.baseclass import BaseEntity

E = TypeVar('E', bound='BaseEntity')
students = [E]


class BaseRepo(Generic[E]):
    def __init__(self, entity: Type[E]) -> None:
        self.entity = entity

    def insert(self, entity: Type[E]):
        global id
        students.append(entity)
        return entity

    @staticmethod
    def get_all() -> list[E]:
        return students

    @staticmethod
    def get(id: int) -> Type[E]:
        stu = None
        for s in students:
            if s['id'] == id:
                stu = s
                break
        if stu is None:
            return None
        else:
            return stu

    @staticmethod
    def update(entity: Type[E], id: int) -> bool:
        status = False
        for s in students:
            if s == id:
                status = True
                s = entity
                break
        return status

    @staticmethod
    def delete(id) -> bool:
        status = False
        for s in students:
            if s.id == id:
                status = True
                students.pop(s['id'])
                break
        return status
