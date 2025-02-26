from entities.baseclass import BaseEntity
from dataclasses import dataclass


@dataclass
class student(BaseEntity):
    name: str
    age: str
    grade: str
