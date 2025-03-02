from infrastructure.base_repo import BaseRepo
from domain.student_entity import Student


class StudentRepo(BaseRepo[Student]):
    def __init__(self) -> None:
        super().__init__(Student)
