from typing import Optional
from flask import abort, jsonify, request, Response
from flask.views import MethodView
from application.services.teachers import TeacherServices
from domain.entities.teacher_entity import Teacher
from infrastructure.repository.teacher_repo import TeacherRepo
from typing import Dict, Any


class TeacherView(MethodView):
    def __init__(self) -> None:
        self.teacher_repo = TeacherRepo()
        self.service = TeacherServices(self.teacher_repo)

    def get(self, id: Optional[int] = None) -> Response:
        if id is None:
            all_teacher: list[Dict[str, Any]] = self.service.get_all(self.teacher_repo)
            return jsonify(all_teacher)
        else:
            teacher: Dict[str, Any] | None = self.service.get_by_id(int(id), self.teacher_repo)
            if teacher is None:
                abort(404, description='Student not found')
                return None
            return jsonify(teacher)

    def post(self) -> Response | None:
        data = request.get_json()
        if not data:
            abort(400, description='Invalid data')

        entity = Teacher(
            id=None,
            name=data.get('name'),
            age=data.get('age'),
            subject=data.get('subject')
        )
        if not all([entity.name, entity.age, entity.subject]):
            abort(400, description='Required fields missing')
            return None

        result = self.service.add(entity, self.teacher_repo)
        if result:
            return jsonify(vars(result))
        abort(500, description='Error adding teacher')

    def put(self, id: int) -> Response | None:
        data = request.get_json()
        if not data:
            abort(400, description='Invalid JSON data')
            return None

        entity = Teacher(
            id=None,
            name=data.get('name'),
            age=data.get('age'),
            subject=data.get('subject')
        )
        result = self.service.update(id, entity, self.teacher_repo)
        if not result:
            abort(404, description='teacher not found')
            return None

        return jsonify(message='teacher updated successfully')

    def delete(self, id: int) -> Response | None:
        result = self.service.delete(id, self.teacher_repo)
        if not result:
            abort(404, description='teacher not found')
            return None

        return jsonify(message='teacher deleted successfully')
