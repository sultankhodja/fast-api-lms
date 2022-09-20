import fastapi
from pydantic import BaseModel
from typing import Optional, List

router = fastapi.APIRouter()


users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@router.get("/users", response_model=List[User])  # defining routes
async def get_users():
    return users


@router.post("/users")  # defining routes
async def create_users(user: User):
    users.append(user)
    return "Success"


@router.get("/users/{id}")
async def get_user(id:int):
    return {"users": users[id]}


