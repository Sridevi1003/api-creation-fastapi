from fastapi import FastAPI
from pydantic import BaseModel


class Movie(BaseModel):
    name: str
    description: str
    rating: int


app = FastAPI()

DATABASE = {
    1: {"name": "iron_man_1", "description": "the rise of mr. tony", "rating": 8},
    2: {"name": "iron_man_2", "description": "tony & rhodey fight", "rating": 7},
    3: {"name": "iron_man_3", "description": "multiple iron mechs", "rating": 10},
    4: {"name": "avengers_1", "description": "avengers, assemble!", "rating": 9},
    5: {"name": "avengers_2", "description": "ultron attacks fast", "rating": 9}
}


@app.get("/")
async def get_all_movies():
    return DATABASE


@app.get("/{movie_id}")
async def get_movie_info_by_id(movie_id: int):
    return DATABASE.get(movie_id, {"message": "Movie not found"})


@app.post("/{movie_id}")
async def add_movie(movie: Movie):
    key = len(DATABASE) + 1
    DATABASE[key] = movie.dict()
    return {"message": "Movie added"}


@app.put("/{movie_id}")
async def edit_movie_info(movie_id: int, movie: Movie):
    if movie_id in DATABASE:
        DATABASE[movie_id] = movie.dict()
        return {"message": "Movie updated"}
    else:
        return {"message": "Movie not found"}


@app.delete("/{movie_id}")
async def delete_movie(movie_id: int):
    if movie_id in DATABASE:
        del DATABASE[movie_id]
        return {"message": "Movie deleted"}
    else:
        return {"message": "Movie not found"}
