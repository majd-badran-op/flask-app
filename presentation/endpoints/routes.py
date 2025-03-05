from flask import Flask
from .teacher_view import TeacherView
from .student_view import StudentView
from .student_teacher_view import StudentTeacherView


def register_routes(app: Flask) -> None:

    student_view = StudentView.as_view('student_view')
    app.add_url_rule('/students', view_func=student_view, methods=['GET', 'POST'])
    app.add_url_rule('/students/<int:id>', view_func=student_view, methods=['GET', 'PUT', 'DELETE'])

    teacher_view = TeacherView.as_view('teacher_view')
    app.add_url_rule('/teachers', view_func=teacher_view, methods=['GET', 'POST'])
    app.add_url_rule('/teachers/<int:id>', view_func=teacher_view, methods=['GET', 'PUT', 'DELETE'])

    student_teacher_view = StudentTeacherView.as_view('student_teacher_view')
    app.add_url_rule('/student_teacher', view_func=student_teacher_view, methods=['GET', 'POST'])
    app.add_url_rule('/student_teacher/<int:id>', view_func=student_teacher_view, methods=['GET', 'PUT', 'DELETE'])
