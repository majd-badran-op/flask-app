from .base_repo import BaseRepo
from domain.aggregates.student_teacher import StudentTeacher
from infrastructure.database.schema import student_teacher


class StudentTeacherRepo(BaseRepo[StudentTeacher]):
    def __init__(self) -> None:
        super().__init__(StudentTeacher, student_teacher)
