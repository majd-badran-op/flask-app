from entities.baseclass import BaseEntity


class student(BaseEntity):
    name: str
    age: str
    grade: str

    def __init__(self, id: int, name: str, age: str, grade: str):
        super().__init__(id)
        self.name = name
        self.age = age
        self.grade = grade

    def get_id(self):
        return self.id
