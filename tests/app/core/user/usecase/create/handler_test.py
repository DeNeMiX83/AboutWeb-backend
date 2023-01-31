import pytest
from app.core.user.usecase.register import RegisterUserUseCase


@pytest.mark.usefixtures("users")
def test_create_user_handler(users):
    handler = RegisterUserUseCase()
    for user in users:
        handler.execute(user)