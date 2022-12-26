import pytest
from pathlib import Path
from app.core.shared.entities.value_objects import UUID
from app.core.user.entities.user import *

class UserTest():
    def test_user(self):
        UserEntity(
            id=UUID('8683bc3d-5d57-4956-8975-e573bb7bafd1'),
            username=UserName('test'),
            email=Email('testemail@gmail.com'),
            password=Password('TestPassword1!'),
            posts=[Post('backend')],
            avatar=Image(Path('tests/app/core/user/entities/data/test_image.png'))
        )