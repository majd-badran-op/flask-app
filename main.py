from flask import Flask, abort, jsonify, request
from flask.views import MethodView

from applecation.students import students_controller

app = Flask(__name__)


class StudentView(MethodView):
    def get(self, id=None):
        if id is None:
            result = students_controller.get_all()
            return jsonify(result)
        result = students_controller.get_by_id(id)
        if result is None:
            abort(404, description='Student not found')
        return jsonify(result=result)

    def post(self):
        data = request.get_json()
        result = students_controller.add_student(data)
        if result:
            return jsonify(result=vars(result))
        abort(400, description='required key missing')

    def put(self, id):
        data = request.get_json()
        result = students_controller.update(id, data)
        if result:
            abort(404, description='Student not found')
        return jsonify(message='Student updated successfully')

    def delete(self, id):
        result = students_controller.delete(id)
        if result:
            abort(404, description='student not found')
        return jsonify(message='Student deleted successfully')


student_view = StudentView.as_view('student_view')
app.add_url_rule('/students', view_func=student_view, methods=['GET', 'POST'])
app.add_url_rule('/students/<int:id>',
                 view_func=student_view, methods=['GET', 'PUT', 'DELETE'])

if __name__ == '__main__':
    app.run(debug=True)
