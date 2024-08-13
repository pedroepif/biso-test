from faker import Faker
from sqlalchemy.orm import Session
from src.controller.database import localSession, engine, Base
from src.models.movie import Movie
from src.models.user import User
from src.models.view import View
import random

fake = Faker()

def populate():
  db: Session = localSession()

  try:
    for _ in range(100):
      movie = Movie(
        title = fake.catch_phrase(),
        genre = fake.word(ext_word_list=["Action", "Comedy", "Drama", "Horror"]),
        director = fake.name(),
        actors = ", ".join(fake.name() for _ in range(5))
      )
      db.add(movie)
    db.commit()

    for _ in range(20):
      user = User(
        name = fake.name()
      )
      db.add(user)
    db.commit()

    movie_ids = [movie.id for movie in db.query(Movie.id).all()]
    user_ids = [user.id for user in db.query(User.id).all()]

    for _ in range(500):
      view = View(
        user_id = random.choice(user_ids),
        movie_id = random.choice(movie_ids),
        rating = random.uniform(1, 5) if random.choice([True, False]) else None
      )
      db.add(view)
    db.commit()
  finally:
    db.close()

if __name__ == "__main__":
  Base.metadata.create_all(bind=engine)
  populate()