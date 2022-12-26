import pytest
from pathlib import Path
import json

from app.core.user.dto.user import UserDto
from app.core.user.entities.value_objects import *
from app.core.shared.entities.value_objects import Image

@pytest.fixture
def users():
    users = []
    with open('tests/app/core/user/entities/data/users_test.json', 'r') as f:
        users = map(lambda user: UserDto(**user), json.load(f))
    return users