from dataclasses import dataclass, field
from typing import List
from app.core.user.entities import value_objects as vo
from app.core.shared.entities import value_objects as shared_vo
from app.core.shared.entities.entity import Entity

@dataclass()
class User(Entity):
    id: vo.UserID
    username: vo.UserName
    email: vo.Email
    password: vo.HashedPassword
    avatar: shared_vo.Image
    posts: List[vo.Post] = field(default_factory=list)
