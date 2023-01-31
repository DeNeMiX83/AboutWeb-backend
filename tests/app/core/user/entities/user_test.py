from pathlib import Path
from app.core.user.entities import value_objects as vo
from app.core.shared.entities import value_objects as shared_vo
from app.core.user import entities


class UserTest():
    def test_user(self):
        entities.User(
            id=vo.UUID('8683bc3d-5d57-4956-8975-e573bb7bafd1'),
            username=vo.UserName('test'),
            email=vo.Email('testemail@gmail.com'),
            password=vo.HashedPassword('8683bc3d-5d57-4956-8975-e573bb7bafd1'),
            posts=[vo.Post('backend')],
            avatar=shared_vo.Image(Path('tests/app/core/user/entities/data/test_image.png'))
        )