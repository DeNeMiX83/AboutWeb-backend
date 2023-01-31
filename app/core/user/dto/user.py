from typing import List
from app.shared.dto import BaseDto


class User(BaseDto):
    username: str
    email: str
    password: str
    avatar: str
    posts: List[str] = []