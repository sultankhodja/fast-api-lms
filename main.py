from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(
    title="Fast API, LMS",
    description="LMS for managing students and courses",
    contact={
        'name': 'Azim',
        'email': 'azimsultnkhodjaev@gmail.com'
    }
)

users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/users", response_model=List[User])  # defining routes
async def get_users():
    return users


@app.post("/users")  # defining routes
async def create_users(user: User):
    users.append(user)
    return "Success"


@app.get("/users/{id}")
async def get_user(
            id: int = Path(..., description="The ID of the user you want to retrieve.", gt=2),  # description of API
            q: str = Query(None, max_length=5)):
    return {"user": users[id], "query": q}














