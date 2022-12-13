import pytest
from pathlib import Path
from app.entities.user.user import *

class UserTest():
    def test_user(self):
        User(
            id=UUID('8683bc3d-5d57-4956-8975-e573bb7bafd1'),
            username='test_username',
            email=Email('testemail@gmail.com'),
            password=Password('TestPassword1!'),
            post=Post.BACKEND,
            avatar=Image(Path('app/tests/entities/base/test_image.png'))
        )