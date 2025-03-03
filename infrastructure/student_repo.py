from infrastructure.base_repo import BaseRepo
from domain.student_entity import Student
from database.schema import students


class StudentRepo(BaseRepo[Student]):
    def __init__(self) -> None:
        super().__init__(Student, students)
