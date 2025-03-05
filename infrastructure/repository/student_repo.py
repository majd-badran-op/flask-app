from .base_repo import BaseRepo
from domain.student_entity import Student
from infrastructure.database.schema import students
from infrastructure.database.con import get_session


class StudentRepo(BaseRepo[Student]):
    def __init__(self) -> None:
        super().__init__(Student, students, get_session())
