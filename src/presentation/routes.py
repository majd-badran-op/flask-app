from flask import Flask
from .view.teacher_view import TeacherView
from .view.student_view import StudentView
from flask_cors import CORS


def register_routes(app: Flask):
    student_view = StudentView.as_view('student_view')

    app.add_url_rule('/students', view_func=student_view, methods=['GET', 'POST'])
    app.add_url_rule('/students/<int:id>', view_func=student_view, methods=['GET', 'PUT', 'DELETE'])

    teacher_view = TeacherView.as_view('teacher_view')
    app.add_url_rule('/teachers', view_func=teacher_view, methods=['GET', 'POST'])
    app.add_url_rule('/teachers/<int:id>', view_func=teacher_view, methods=['GET', 'PUT', 'DELETE'])


def setup_cors(app):
    CORS(app, resources={r'/*': {'origins': '*'}}, methods=['GET', 'POST', 'PUT', 'DELETE'])
