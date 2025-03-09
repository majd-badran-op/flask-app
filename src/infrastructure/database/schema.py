from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

students = Table(
    'students', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('age', Integer),
    Column('grade', Integer),
)

teachers = Table(  # Fixed variable name (was 'teacher')
    'teachers', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('age', Integer),
    Column('subject', String)
)
