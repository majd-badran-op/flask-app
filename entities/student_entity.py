from entities.baseclass import BaseEntity


class student(BaseEntity):
    def __init__(self, id: int, name: str, age: int, grade: str):
        self.name = name
        self.age = age
        self.grade = grade
        super().__init__(id)
