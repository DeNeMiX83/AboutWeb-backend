from dataclasses import dataclass, field
from typing import List
from .value_objects import *
from app.core.shared.entities.value_objects import Image
from app.core.shared.entities.entity import Entity

@dataclass()
class UserEntity(Entity):
    username: UserName
    email: Email
    password: Password
    avatar: Image
    posts: List[Post] = field(default_factory=list)
