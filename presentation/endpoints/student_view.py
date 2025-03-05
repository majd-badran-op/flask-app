from typing import Optional
from flask import Flask, abort, jsonify, request, Response
from flask.views import MethodView
from application.services.students import StudentServices
from domain.student_entity import Student
from infrastructure.repository.student_repo import StudentRepo
from typing import Dict, Any


class StudentView(MethodView):
    def __init__(self) -> None:
        student_repo = StudentRepo()
        self.service = StudentServices(student_repo)

    def get(self, id: Optional[int] = None) -> Response:
        if id is None:
            all_students: list[Dict[str, Any]] = self.service.get_all()
            return jsonify(all_students)
        else:
            student: Dict[str, Any] | None = self.service.get_by_id(int(id))
            if student is None:
                abort(404, description='Student not found')
            return jsonify(student)

    def post(self) -> Response:
        data = request.get_json()
        if not data:
            abort(400, description="Invalid data")

        entity = Student(
            id=None,
            name=data.get('name'),
            age=data.get('age'),
            grade=data.get('grade')
        )
        if not all([entity.name, entity.age, entity.grade]):
            abort(400, description='Required fields missing')

        result = self.service.add_student(entity)
        if result:
            return jsonify(vars(result))
        abort(500, description='Error adding student')

    def put(self, id: int) -> Response:
        data = request.get_json()
        if not data:
            abort(400, description="Invalid JSON data")

        result = self.service.update(id, data)
        if not result:
            abort(404, description='Student not found')

        return jsonify(message='Student updated successfully')

    def delete(self, id: int) -> Response:
        result = self.service.delete(id)
        if not result:
            abort(404, description='Student not found')

        return jsonify(message='Student deleted successfully')


def register_routes(app: Flask) -> None:
    student_view = StudentView.as_view('student_view')
    app.add_url_rule('/students', view_func=student_view, methods=['GET', 'POST'])
    app.add_url_rule('/students/<int:id>', view_func=student_view, methods=['GET', 'PUT', 'DELETE'])
