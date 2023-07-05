from typing import Union, Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

active_users: Dict = {}

app = FastAPI()

class User(BaseModel):
    username: str
    x: Union[float, None] = 0.0
    y: Union[float, None] = 0.0

@app.get("/users/")
def get_users() -> Dict:
    return active_users

@app.post("/users/")
def create_user(user: User) -> Dict:
    if not user.username in list(active_users.keys()):
        active_users[user.username] = user

    return active_users

@app.put("/users/")
def move_user(user: User) -> Dict:
    if not user.username in list(active_users.keys()):
        raise HTTPException(status_code=404, detail="User not found")

    active_users[user.username].x = user.x
    active_users[user.username].y = user.y
    
    return active_users