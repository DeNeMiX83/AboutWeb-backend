from app.core.shared.handler import Handler
from app.core.user.dto.user import UserDto
from app.core.user.entities.user import UserEntity

class CreateUserHandler(Handler):
    def __init__(self):
        ...

    def execute(self, user_dto: UserDto) -> None:
        user_id = UserEntity.generate_id()
        user = UserEntity(
            id=user_id,
            **user_dto.dict(exclude={'id'})
        )
        
        # save in db