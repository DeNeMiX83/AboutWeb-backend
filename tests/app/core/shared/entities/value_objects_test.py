import pytest
from pathlib import Path
from app.core.shared.entities.value_objects import *


class ImageTest:

    def test_image_extension(cls):
        with pytest.raises(ImageError) as e_info:
            Image(Path('tests/app/core/shared/entities/data/test_image.txt'))

    def test_image_not_found(cls):
        with pytest.raises(errors.PathNotAFileError) as e_info:
            Image(Path('tests/app/core/shared/entities/data/test_image.jpg'))

    def test_image(cls):
        Image(Path('tests/app/core/shared/entities/data/test_image.png'))


class UUIDTest:
    def test_uuid(cls):
        UUID('123e4567-e89b-12d3-a456-426655440000')

    def test_uuid_error(cls):
        with pytest.raises(ValueError) as e_info:
            UUID('123e4567-e89b-12d3-a456-42665540000')

    def test_uuid_version_1(cls):
        UUID('b69cdc2c-7e4a-11ed-a1eb-0242ac120002')