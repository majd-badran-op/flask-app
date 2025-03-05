from domain.entities.base_class import BaseEntity
from dataclasses import dataclass


@dataclass
class StudentTeacher(BaseEntity):
    student_id: int
    teacher_id: int
    grade: int
