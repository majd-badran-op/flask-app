from entities.student_entity import student
from repo.student_repo import student_repo

id = 1


class students_controller:
    repo = student_repo()

    @staticmethod
    def add_student(data: dict):
        global id
        entity = student(id,
                         data['name'], data['age'], data['grade'])
        result = students_controller.repo.insert(entity)
        id += 1
        return result

    @staticmethod
    def get_all():
        return students_controller.repo.get_all()

    @staticmethod
    def get_by_id(id):
        result = students_controller.repo.get(id)
        if result is None:
            return None
        return students_controller.repo.get(id)

    @staticmethod
    def update(id, data: dict):
        entity = student(data['id'], data['name'], data['age'], data['grade'])
        result = students_controller.repo.update(entity, data['id'])
        if result:
            return None

    @staticmethod
    def delete(id):
        result = students_controller.repo.delete(id)
        return result
