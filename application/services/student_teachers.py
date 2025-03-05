from typing import Any, Dict
from infrastructure.repository.student_teacher_repo import StudentTeacherRepo
from infrastructure.repository.unit_of_work import UnitOfWork
from domain.aggregates.student_teacher import StudentTeacher


class StudentTeacherServes:
    def __init__(self, repo: StudentTeacherRepo) -> None:
        self.repo = repo

    def add_student(self, entity: StudentTeacher) -> StudentTeacher | None:
        with UnitOfWork(self.repo) as uow:
            assert uow.repo is not None
            result = uow.repo.insert(entity, uow.session)
            uow.commit()
            return result

    def get_all(self) -> list[Dict[str, Any]]:
        with UnitOfWork(self.repo) as uow:
            assert uow.repo is not None
            students = uow.repo.get_all(uow.session)
        return [vars(s) for s in students]

    def get_by_id(self, id: int) -> Dict[str, Any] | None:
        with UnitOfWork(self.repo) as uow:
            assert uow.repo is not None
            student_entity = uow.repo.get(id, uow.session)
        return vars(student_entity) if student_entity else None

    def update(self, id: int, data: Dict[str, Any]) -> bool:
        with UnitOfWork(self.repo) as uow:
            assert uow.repo is not None
            student = uow.repo.get(id, uow.session)
            if student is None:
                return False
            student.name = data.get('name', student.name)
            student.age = data.get('age', student.age)
            student.subject = data.get('subject', student.grade)

            uow.repo.update(student, id, uow.session)
            uow.commit()
            return True

    def delete(self, id: int) -> bool:
        with UnitOfWork(self.repo) as uow:
            assert uow.repo is not None
            result = uow.repo.delete(id, uow.session)
            if result:
                uow.commit()
            return result
