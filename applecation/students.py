from entities.student_entity import student
from repo.student_repo import student_repo

id = 1


class students_controller:
    @staticmethod
    def add_student(data: dict):
        global id
        entity = student()
        entity.id = id
        entity.name = data["name"]
        entity.age = data["age"]
        entity.grade = data["grade"]
        repo = student_repo(entity)
        result = repo.insert(entity)
        return result

    @staticmethod
    def get_all():
        return student_repo.get_all()

    @staticmethod
    def get_by_id(id):
        result = student_repo.get(id)
        if result is None:
            return None
        return student_repo.get(id)

    @staticmethod
    def update(id, data: dict):
        entity = student()
        entity.id = data["id"]
        entity.name = data["name"]
        entity.age = data["age"]
        entity.grade = data["grade"]
        result = student_repo.update(id, entity)
        if result:
            return None

    @staticmethod
    def delete(id):
        result = student_repo.delete(id)
        if result is None:
            return None
        return result
