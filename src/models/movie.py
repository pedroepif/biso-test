from sqlalchemy import Column, Integer, String
from src.controller.database import Base

class Movie(Base):
    __tablename__ = "movies"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    genre = Column(String)
    director = Column(String)
    actors = Column(String)