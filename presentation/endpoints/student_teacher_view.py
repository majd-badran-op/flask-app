from typing import Optional
from flask import abort, jsonify, request, Response
from flask.views import MethodView
from application.services.student_teachers import StudentTeacherServes
from infrastructure.repository.student_teacher_repo import StudentTeacherRepo
from domain.aggregates.student_teacher import StudentTeacher
from typing import Dict, Any


class StudentTeacherView(MethodView):
    def __init__(self) -> None:
        teacher_repo = StudentTeacherRepo()
        self.service = StudentTeacherServes(teacher_repo)

    def get(self, id: Optional[int] = None) -> Response:
        if id is None:
            all_teacher: list[Dict[str, Any]] = self.service.get_all()
            return jsonify(all_teacher)
        else:
            teacher: Dict[str, Any] | None = self.service.get_by_id(int(id))
            if teacher is None:
                abort(404, description='subject not found')
                return None
            return jsonify(teacher)

    def post(self) -> Response | None:
        data = request.get_json()
        if not data:
            abort(400, description="Invalid data")

        entity = StudentTeacher(
            id=None,
            student_id=data.get('student_id'),
            teacher_id=data.get('teacher_id'),
            grade=data.get('grade')
        )
        if not all([entity.student_id, entity.teacher_id, entity.grade]):
            abort(400, description='Required fields missing')
            return None

        result = self.service.add_student(entity)
        if result:
            return jsonify(vars(result))
        abort(500, description='Error adding subject')

    def put(self, id: int) -> Response | None:
        data = request.get_json()
        if not data:
            abort(400, description="Invalid JSON data")
            return None

        result = self.service.update(id, data)
        if not result:
            abort(404, description='subject not found')
            return None

        return jsonify(message='subject updated successfully')

    def delete(self, id: int) -> Response | None:
        result = self.service.delete(id)
        if not result:
            abort(404, description='subject not found')
            return None

        return jsonify(message='subject deleted successfully')
