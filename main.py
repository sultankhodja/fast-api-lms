from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List
from api import users, courses, sections

app = FastAPI(
    title="Fast API, LMS",
    description="LMS for managing students and courses",
    contact={
        'name': 'Azim',
        'email': 'azimsultnkhodjaev@gmail.com'
    }
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)















