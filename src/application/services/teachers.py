from infrastructure.repository.teacher_repo import TeacherRepo
from .base_service import BaseService


class TeacherServices(BaseService):
    def __init__(self, repo: TeacherRepo) -> None:
        self.repo = repo
