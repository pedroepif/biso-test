from sqlalchemy.orm import Session
from src.models.movie import Movie
from src.models.view import View
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict
import numpy as np

def getMovies(db: Session):
  try:
    movies = db.query(Movie).all()
    movieData = [{
      "id": movie.id,
      "title": movie.title,
      "genre": movie.genre,
      "director": movie.director,
      "actors": movie.actors
    } for movie in movies]
    return movieData
  except Exception as e:
    return {"error": str(e)}

def prepareCorpus(movieData: List[Dict]):
  return [f"{movie['genre']} {movie['director']} {' '.join(movie['actors'].split(', '))}" for movie in movieData]

def getUserPreferences(db: Session, user_id: int):
  try:
    userViews = db.query(View).filter(View.user_id == user_id).all()
    if not userViews:
      return {"message": "No data available for this user"} 

    moviesIds = [view.movie_id for view in userViews]
    ratings = {view.movie_id: view.rating for view in userViews}

    movies = db.query(Movie).filter(Movie.id.in_(moviesIds)).all()
    genders = {movie.genre for movie in movies}
    directors = {movie.director for movie in movies}
    actors = {actor for movie in movies for actor in movie.actors.split(", ")}

    return {
      "movieIds": moviesIds,
      "ratings": ratings,
      "genders": list(genders),
      "directors": list(directors),
      "actors": list(actors)
    }
  except Exception as e:
    return {"error": str(e)}

def userRecommendation(db: Session, user_id: int):
  userPreferences = getUserPreferences(db, user_id)

  if "message" in userPreferences:
    return userPreferences["message"]

  try:
    movieData = getMovies(db)
    corpus = prepareCorpus(movieData)

    vectorizer = TfidfVectorizer()
    tfidfMatrix = vectorizer.fit_transform(corpus)

    userMovieIds = userPreferences["movieIds"]
    userMovieIndex = [i for i, movie in enumerate(movieData) if movie["id"] in userMovieIds]

    if not userMovieIndex:
      return {"message": "No recommendations available based on user's history"}
    
    userMovieIndex = np.array(userMovieIndex)
    userProfile = tfidfMatrix[userMovieIndex].mean(axis=0)
    userProfile = np.asarray(userProfile).reshape(1, -1)

    cosineSimilarities = cosine_similarity(userProfile, tfidfMatrix).flatten()

    similarIndices = cosineSimilarities.argsort()[-10:][::-1]

    recommendedMovies = [movieData[i] for i in similarIndices]

    return recommendedMovies
  except Exception as e:
    return {"error": str(e)}
  
  




