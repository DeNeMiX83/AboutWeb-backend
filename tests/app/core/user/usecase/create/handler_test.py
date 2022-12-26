import pytest
from app.core.user.usecase.create.handler import CreateUserHandler


@pytest.mark.usefixtures("users")
def test_create_user_handler(users):
    handler = CreateUserHandler()
    for user in users:
        handler.execute(user)