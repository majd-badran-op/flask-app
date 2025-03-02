from typing import Any, Dict
from entities.student_entity import Student
from repo.student_repo import StudentRepo


class StudentServices:
    repo = StudentRepo()
    id = 1

    @staticmethod
    def add_student(data: Dict[str, Any]) -> Student:
        entity = Student(
            StudentServices.id, data['name'], data['age'], data['grade']
        )
        StudentServices.id += 1
        return StudentServices.repo.insert(entity)

    @classmethod
    def get_all(cls) -> list[Dict[str, Any]]:
        return [vars(s) for s in cls.repo.get_all()]

    @classmethod
    def get_by_id(cls, id: int) -> Dict[str, Any] | None:
        student_entity = cls.repo.get(id)
        if student_entity:
            return vars(student_entity)
        return None

    @classmethod
    def update(cls, id: int, data: Dict[str, Any]) -> bool:
        entity = Student(id, data['name'], data['age'], data['grade'])
        return cls.repo.update(entity, id)

    @classmethod
    def delete(cls, id: int) -> bool:
        return cls.repo.delete(id)
