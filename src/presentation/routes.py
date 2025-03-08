from flask import Flask
from .view.teacher_view import TeacherView
from .view.student_view import StudentView


def register_routes(app: Flask) -> None:

    student_view = StudentView.as_view('student_view')
    app.add_url_rule('/students', view_func=student_view, methods=['GET', 'POST'])
    app.add_url_rule('/students/<int:id>', view_func=student_view, methods=['GET', 'PUT', 'DELETE'])

    teacher_view = TeacherView.as_view('teacher_view')
    app.add_url_rule('/teachers', view_func=teacher_view, methods=['GET', 'POST'])
    app.add_url_rule('/teachers/<int:id>', view_func=teacher_view, methods=['GET', 'PUT', 'DELETE'])
