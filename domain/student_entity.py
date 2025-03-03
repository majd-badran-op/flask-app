from domain.baseclass import BaseEntity
from dataclasses import dataclass


@dataclass
class Student(BaseEntity):
    name: str
    age: int
    grade: int
