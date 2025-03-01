from typing import Generic, TypeVar, Type, Any
from entities.baseclass import BaseEntity

E = TypeVar('E', bound='BaseEntity')


class BaseRepo(Generic[E]):
    students: list[dict[str, E]] = []

    def __init__(self, entity: Type[E]) -> None:
        self.entity = entity

    @classmethod
    def insert(cls, entity: E) -> E:
        new_student: dict[str, E] = {str(entity.id): entity}
        cls.students.append(new_student)
        return entity

    @classmethod
    def get_all(cls) -> list[E]:
        return [list(student.values())[0] for student in cls.students]

    @classmethod
    def get(cls, id: int) -> E | None | Any:
        id_str = str(id)
        for student_dict in cls.students:
            if id_str in student_dict:
                return student_dict[id_str]
        return None

    @classmethod
    def update(cls, entity: E, id: int) -> bool:
        id_str = str(id)
        for i, student_dict in enumerate(cls.students):
            if id_str in student_dict:
                cls.students[i] = {id_str: entity}
                return True
        return False

    @classmethod
    def delete(cls, id: int) -> bool:
        id_str = str(id)
        for i, student_dict in enumerate(cls.students):
            if id_str in student_dict:
                cls.students.pop(i)
                return True
        return False
