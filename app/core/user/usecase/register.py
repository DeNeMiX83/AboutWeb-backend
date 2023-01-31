from app.core.shared.usecase.usecase import UseCase
from app.core.user.dto import user as dto
from app.core.user import entities

class RegisterUserUseCase(UseCase):
    def __init__(self):
        ...

    def execute(self, user_dto: dto.User) -> None:
        user = entities.User(
            id=entities.User.generate_id(),
            **user_dto.dict(exclude={'id'})
        )

        
        
        # save in db