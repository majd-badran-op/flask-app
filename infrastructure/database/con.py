from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import os


DATABASE_URL = os.getenv('DATABASE_URL') or ''
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_session() -> Session:
    return SessionLocal()
