from flask import Flask, request, jsonify, abort

app = Flask(__name__)
students = []
id = 1


class StudentView:
    @app.route('/students/create_student', methods=['POST'])
    def create_student(self):
        global id
        data = request.get_json()
        if len(data.keys()) == 4:
            student = {
                'id': id,
                'name': data['name'],
                'age': data['age'],
                'grade': data['grade']
            }
            students.append(student)
            id += 1
            return jsonify(student, message='a new student was added')
        else:
            abort(400, description='required key missing')

    @app.route('/students', methods=['GET'])
    def get_students(self):
        return jsonify(students)

    @app.route('/students/<int:id>', methods=['GET'])
    def get_student(self, id):
        student = None
        for s in students:
            if s['id'] == id:
                student = s
                break
        if student is None:
            abort(404, description='student not found')
        return jsonify(students)

    @app.route('/students/update_student/<int:id>', methods=['PUT'])
    def update_student(self, id):
        student = None
        for s in students:
            if s["id"] == id:
                student = s
                break
        if student is None:
            abort(404, description="student not found")

        data = request.get_json()
        student['name'] = data['name']
        student['age'] = data['age']
        student['grade'] = data['grade']
        return jsonify(students)

    @app.route('/students/<int:id>', methods=['DELETE'])
    def delete_student(self, id):
        student = None
        for s in students:
            if s['id'] == id:
                student = s
                break
        if student is None:
            abort(404, description="student not found")

        students.remove(student)
        return jsonify(message=f'student with id {id} was deleted')
