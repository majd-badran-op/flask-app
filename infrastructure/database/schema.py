from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from .con import engine

metadata = MetaData()

students = Table(
    'students', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('age', Integer)
)

teacher = Table(
    'teachers', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('age', Integer),
    Column('subject', String)
)

student_teacher = Table(
    'students_teachers', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('teacher_id', Integer, ForeignKey('teachers.id')),
    Column('grade', Integer)
)

metadata.create_all(engine)
