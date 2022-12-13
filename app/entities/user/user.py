from dataclasses import dataclass
from .value_objects import *
from app.entities.base.value_objects import Image, UUID

@dataclass()
class User():
    id: UUID
    username: UserName
    email: Email
    password: Password
    post: Post
    avatar: Image



