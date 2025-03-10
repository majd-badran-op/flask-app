from .base_repo import BaseRepo
from domain.entities.teacher_entity import Teacher
from infrastructure.database.schema import teachers


class TeacherRepo(BaseRepo[Teacher]):
    def __init__(self) -> None:
        super().__init__(Teacher, teachers)
