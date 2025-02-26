from flask import Flask, request, jsonify, abort
from applecation.students import students_controller

app = Flask(__name__)


class StudentView:
    @app.route('/students/create_student', methods=['POST'])
    @staticmethod
    def insert_student():
        data = request.get_json()
        result = students_controller.add_student(data)
        if result:
            return jsonify(result=vars(result))
        else:
            abort(400, description='Required key missing')

    @app.route('/students', methods=['GET'])
    @staticmethod
    def get_students():
        result = students_controller.get_all()
        return jsonify(result=result)

    @app.route('/students/<int:id>', methods=['GET'])
    @staticmethod
    def get_student(id):
        result = students_controller.get_by_id(id)
        if result is None:
            abort(404, description='Student not found')
        return jsonify(result=result)

    @app.route('/students/update_student/<int:id>', methods=['PUT'])
    @staticmethod
    def update_student(id):
        data = request.get_json()
        result = students_controller.update(id, data)
        if not result:
            abort(404, description='Student not found')

    @app.route('/students/delete_student/<int:id>', methods=['DELETE'])
    @staticmethod
    def delete_student(id):
        result = students_controller.delete(id)
        if not result:
            abort(404, description='Student not found')


if __name__ == '__main__':
    app.run(debug=True)
