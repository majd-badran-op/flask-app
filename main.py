from flask import Flask, request, jsonify, abort
from applecation.students import students_controller

app = Flask(__name__)


class StudentView:
    @app.route('/students/create_student', methods=['POST'])
    def insert_student():
        data = request.get_json()
        result = students_controller.add_student(data)
        if result:
            return jsonify(result=vars(result))
        else:
            abort(400, description='Required key missing')

    @app.route('/students', methods=['GET'])
    def get_students():
        result = students_controller.get_all()
        return jsonify(result=result)

    @app.route('/students/<int:id>', methods=['GET'])
    def get_student(self, id):
        result = students_controller.get_by_id(id)
        if result is None:
            abort(404, description='student not found')
        return jsonify(result=result)

    @app.route('/students/update_student/<int:id>', methods=['PUT'])
    def update_student(self, id):
        data = request.get_json()
        result = students_controller.update(id, data)
        if result:
            abort(404, description='student not found')

    @app.route('/students/delete_student/<int:id>', methods=['DELETE'])
    def delete_student(self, id):
        result = students_controller.delete(id)
        if result:
            abort(404, description='student not found')


if __name__ == '__main__':
    app.run(debug=True)
