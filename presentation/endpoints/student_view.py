from typing import Optional
from flask import abort, jsonify, request, Response
from flask.views import MethodView
from application.services.students import StudentServices
from domain.student_entity import Student


class StudentView(MethodView):
    def __init__(self, service: StudentServices) -> None:
        self.service = service

    def get(self, id: Optional[int] = None) -> Response:
        if id is None:
            result = self.service.get_all()
            return jsonify(result)
        else:
            result = self.service.get_by_id(int(id))
            if result is None:
                abort(404, description='Student not found')
            return jsonify(result)

    def post(self) -> Response:
        data = request.get_json()
        if not data:
            abort(400, description="Invalid JSON data")

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
            return jsonify(vars(result)), 201
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


def register_routes(app, service: StudentServices):
    student_view = StudentView.as_view('student_view', service)
    app.add_url_rule('/students', view_func=student_view, methods=['GET', 'POST'])
    app.add_url_rule('/students/<int:id>', view_func=student_view, methods=['GET', 'PUT', 'DELETE'])
