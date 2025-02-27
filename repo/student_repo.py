from repo.base_repo import BaseRepo
from entities.student_entity import student


class student_repo(BaseRepo[student]):
    def __init__(self) -> None:
        super().__init__(student)
