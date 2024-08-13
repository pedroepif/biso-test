# controller/api.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.controller.database import Database
from src.controller.recommendation import userRecommendation
from src.models.movie import Movie

router = APIRouter()

@router.get("/movies")
def listMovies(db: Session = Depends(Database)):
    try:
        movies = db.query(Movie).all()
        return movies
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/movies/{user_id}/recommendation")
def recommendation(user_id: int, db: Session = Depends(Database)):
    try:
        recommendedMovies = userRecommendation(db, user_id)
        if isinstance(recommendedMovies, dict) and "message" in recommendedMovies:
            raise HTTPException(status_code=404, detail=recommendedMovies["message"])
        return recommendedMovies
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
