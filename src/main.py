from fastapi import FastAPI
from src.controller import api

app = FastAPI()
app.include_router(api.router)

@app.get("/")
def root():
  return {"message": "Movies recommendation API is ready to use!"}