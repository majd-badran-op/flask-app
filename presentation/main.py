from flask import Flask
from application.services.students import StudentServices
from infrastructure.repository.student_repo import StudentRepo
from .endpoints.student_view import register_routes

app = Flask(__name__)

student_repo = StudentRepo()
student_service = StudentServices(student_repo)

register_routes(app, student_service)

if __name__ == '__main__':
    app.run(debug=True)
