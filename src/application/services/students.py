from infrastructure.repository.student_repo import StudentRepo
from .base_service import BaseService


class StudentServices(BaseService):
    def __init__(self, repo: StudentRepo) -> None:
        self.repo = repo
