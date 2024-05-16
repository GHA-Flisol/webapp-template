from typing import List
from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException
from src.models import Gender, Role, User, UpdateUser
import uvicorn

app = FastAPI()
db: List[User] = [
    User(
        id=str(uuid4()),
        first_name="John",
        last_name="Doe",
        gender=Gender.male,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="Jane",
        last_name="Doe",
        gender=Gender.female,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="James",
        last_name="Gabriel",
        gender=Gender.male,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="Eunit",
        last_name="Eunit",
        gender=Gender.male,
        roles=[Role.admin, Role.user],
    ),
]


#@app.get("/")
#async def root_hello():
#    return "Hello world"


@app.get("/api/v1/all_users")
async def get_all_users():
    return db


@app.get("/api/v1/user/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return {"id": user.id}
    raise HTTPException(status_code=404, detail=f"User with id {id} not found.")


@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{id}")
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404, detail=f"Delete user failed, id {id} not found."
    )


@app.put("/api/v1/users/{id}")
async def update_user(user_update: UpdateUser, id: UUID):
    for user in db:
        if user.id == id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return user.id
    raise HTTPException(status_code=404, detail=f"Could not find user with id: {id}")


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
