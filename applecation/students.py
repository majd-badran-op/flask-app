from typing import Any, Dict
from entities.student_entity import student
from repo.student_repo import student_repo


class students_controller:
    repo = student_repo()
    id = 1

    @staticmethod
    def add_student(data: Dict[str, Any]) -> student:
        entity = student(
            students_controller.id, data['name'], data['age'], data['grade']
        )
        students_controller.id += 1
        return students_controller.repo.insert(entity)

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
        entity = student(data['id'], data['name'], data['age'], data['grade'])
        return cls.repo.update(entity, id)

    @classmethod
    def delete(cls, id: int) -> bool:
        return cls.repo.delete(id)
