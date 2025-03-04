from typing import Any, Dict
from domain.student_entity import Student
from infrastructure.repository.student_repo import StudentRepo


class StudentServices:
    repo = StudentRepo()

    @staticmethod
    def add_student(data: Dict[str, Any]) -> Student | None:
        entity = Student(
            id=None,
            name=data['name'],
            age=data['age'],
            grade=data['grade']
        )
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
        student = cls.repo.get(id)
        if student is None:
            return False
        if 'name' in data and data['name'] != student.name:
            student.name = data['name']
        if 'age' in data and data['age'] != student.age:
            student.age = data['age']
        if 'grade' in data and data['grade'] != student.grade:
            student.grade = data["grade"]
        return cls.repo.update(student, id)

    @classmethod
    def delete(cls, id: int) -> bool:
        return cls.repo.delete(id)
