from typing import Any, Dict
from infrastructure.repository.student_repo import StudentRepo
from infrastructure.repository.unit_of_work import UnitOfWork
from domain.student_entity import Student


class StudentServices:
    def __init__(self, repo: StudentRepo) -> None:
        self.repo = repo

    def add_student(self, entity: Student) -> Student | None:
        with UnitOfWork() as uow:
            result = uow.repo.insert(entity)
            uow.commit()
            return result

    def get_all(self) -> list[Dict[str, Any]]:
        with UnitOfWork() as uow:
            students = uow.repo.get_all()
        return [vars(s) for s in students]

    def get_by_id(self, id: int) -> Dict[str, Any] | None:
        with UnitOfWork() as uow:
            student_entity = uow.repo.get(id)
        return vars(student_entity) if student_entity else None

    def update(self, id: int, data: Dict[str, Any]) -> bool:
        with UnitOfWork() as uow:
            student = uow.repo.get(id)
            if student is None:
                return False

            student.name = data.get('name', student.name)
            student.age = data.get('age', student.age)
            student.grade = data.get('grade', student.grade)

            uow.repo.update(student, id)
            uow.commit()
            return True

    def delete(self, id: int) -> bool:
        with UnitOfWork() as uow:
            result = uow.repo.delete(id)
            if result:
                uow.commit()
            return result
