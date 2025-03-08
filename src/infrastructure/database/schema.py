from sqlalchemy import Table, Column, Integer, String, MetaData
from .con import engine

metadata = MetaData()

students = Table(
    'students', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('age', Integer),
    Column('grade', Integer),
)

teacher = Table(
    'teachers', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('age', Integer),
    Column('subject', String)
)


metadata.create_all(engine)
