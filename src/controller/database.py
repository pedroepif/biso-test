from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./local.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
localSession = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()

def Database():
  db = localSession()
  try:
    yield db
  finally:
    db.close()
