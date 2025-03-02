from typing import Any, Optional

from flask import Flask, abort, jsonify, request
from flask.views import MethodView

from applecation.students import StudentServices

app = Flask(__name__)


class StudentView(MethodView):
    def get(self, id: Optional[int] = None) -> Any:
        if id is None:
            result: list[dict[str, Any]] | dict[str, Any] | None = StudentServices.get_all()
            return jsonify(result)
        else:
            result = StudentServices.get_by_id(int(id))
            if result is None:
                abort(404, description='Student not found')
            return jsonify(result=result)

    def post(self) -> Any:
        data = request.get_json()
        result = StudentServices.add_student(data)
        if result:
            return jsonify(result=vars(result))
        abort(400, description='required key missing')

    def put(self, id: int) -> Any:
        data = request.get_json()
        result = StudentServices.update(id, data)
        if result is False:
            abort(404, description='Student not found')
        return jsonify(message='Student updated successfully')

    def delete(self, id: int) -> Any:
        result = StudentServices.delete(id)
        if result is False:
            abort(404, description='student not found')
        return jsonify(message='Student deleted successfully')


student_view = StudentView.as_view('student_view')
app.add_url_rule('/students', view_func=student_view, methods=['GET', 'POST'])
app.add_url_rule('/students/<int:id>',
                 view_func=student_view, methods=['GET', 'PUT', 'DELETE'])

if __name__ == '__main__':
    app.run(debug=True)
