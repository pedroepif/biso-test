from sqlalchemy import Column, Integer, Float, ForeignKey
from src.controller.database import Base

class View(Base):
    __tablename__ = "views"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
    rating = Column(Float, nullable=True)