from .base_repo import BaseRepo
from domain.entities.student_entity import Student
from infrastructure.database.schema import students


class StudentRepo(BaseRepo[Student]):
    def __init__(self) -> None:
        super().__init__(Student, students)
