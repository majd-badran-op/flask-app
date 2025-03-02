from repo.base_repo import BaseRepo
from entities.student_entity import Student


class StudentRepo(BaseRepo[Student]):
    def __init__(self) -> None:
        super().__init__(Student)
