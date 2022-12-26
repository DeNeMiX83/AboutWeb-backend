from typing import List
from app.shared.dto import Dto


class UserDto(Dto):
    username: str
    email: str
    password: str
    avatar: str
    posts: List[str] = []