import pytest
from pathlib import Path
from app.entities.base.value_objects import *


class ImageTest:

    def test_image_extension(cls):
        with pytest.raises(ImageError) as e_info:
            Image(Path('app/tests/entities/base/test_image.txt'))

    def test_image_not_found(cls):
        with pytest.raises(errors.PathNotAFileError) as e_info:
            Image(Path('app/tests/entities/base/test_image.jpg'))

    def test_image(cls):
        Image(Path('app/tests/entities/base/test_image.png'))


class UUIDTest:
    def test_uuid(cls):
        UUID('123e4567-e89b-12d3-a456-426655440000')

    def test_uuid_error(cls):
        with pytest.raises(ValueError) as e_info:
            UUID('123e4567-e89b-12d3-a456-42665540000')