from sqlalchemy import Table, Column, Integer, String, MetaData
from database.con import engine  # Import the engine to create tables

metadata = MetaData()

students = Table(
    'students', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer),
    Column('grade', Integer)
)

metadata.create_all(engine)
