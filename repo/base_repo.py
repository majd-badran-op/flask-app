from typing import Generic, TypeVar, Type
from entities.baseclass import BaseEntity

E = TypeVar('E', bound=BaseEntity)


class BaseRepo(Generic[E]):
    students: dict[str, E] = {}

    def __init__(self, entity: Type[E]) -> None:
        self.entity = entity

    @classmethod
    def insert(cls, entity: E) -> E:
        id_str = str(entity.id)
        for student in cls.students.values():
            if student.name == entity.name and student.age == entity.age:
                raise ValueError('Student with the same name and age already exists')
        cls.students[id_str] = entity
        return entity

    @classmethod
    def get_all(cls) -> list[E]:
        return list(cls.students.values())

    @classmethod
    def get(cls, id: int) -> E | None:
        if str(id) in cls.students:
            return cls.students.get(str(id))
        return None

    @classmethod
    def update(cls, entity: E, id: int) -> bool:
        id_str = str(id)
        if id_str in cls.students:
            cls.students[id_str] = entity
            return True
        return False

    @classmethod
    def delete(cls, id: int) -> bool:
        return cls.students.pop(str(id), None) is not None
