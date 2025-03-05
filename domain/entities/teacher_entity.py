from .base_class import BaseEntity
from dataclasses import dataclass


@dataclass
class Teacher(BaseEntity):
    name: str
    age: int
    subject: str
