from dataclasses import dataclass
from pydantic import errors
from uuid import UUID
from pathlib import Path
from app.core.shared.entities.value_object import ValueObject


@dataclass(frozen=True)
class Image(ValueObject):
    value: Path

    def __post_init__(self):
        if not self.value.is_file():
            raise errors.PathNotAFileError(path=self.value)

        if not self.value.suffix in ['.jpg', '.jpeg', '.png']:
            raise ImageError(path=self.value)
    
    def __repr__(self):
        return f'Image({self.value})'


class ImageError(errors.PathError):
    code = 'image'
    msg_template = 'Path {path} is not a valid image'