from .base_class import BaseEntity
from dataclasses import dataclass


@dataclass
class Student(BaseEntity):
    name: str
    age: int
    grade: str
