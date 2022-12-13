from dataclasses import dataclass
from enum import Enum
import re
from app.entities.base.value_object import ValueObject


@dataclass(frozen=True)
class UserName(ValueObject):
    value: str

    def __post_init__(self):
        v = self.value

        if not isinstance(v, str):
            raise TypeError("Username must be a string")

        if len(v) < 3:
            raise ValueError("Username must be at least 3 characters long")

        if len(v) > 32:
            raise ValueError("Username must be at most 32 characters long")

        if " " in v:
            raise ValueError("Username must not contain spaces")

        if v.isidentifier():
            raise ValueError("Username must not be identifier")

        if v[0].isnumeric():
            raise ValueError("Username must not start with a digit")

        regex = r"[!@#$%^&*\-()_+]+"
        if re.search(regex, v):
            raise ValueError("Username must not contain special characters")

        if v.isnumeric():
            raise ValueError("Username must not be numeric")



@dataclass(frozen=True)
class Email(ValueObject):
    value: str

    def __post_init__(self):
        v = self.value
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if not isinstance(v, str):
            raise TypeError("Email must be a string")

        if not re.fullmatch(regex, v):
            raise ValueError("Email must be valid")

@dataclass(frozen=True)
class Password(ValueObject):
    value: str

    def __post_init__(self):
        v = self.value

        if not isinstance(v, str):
            raise TypeError("Password must be a string")

        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")

        if len(v) > 32:
            raise ValueError("Password must be at most 32 characters long")

        if not any(char.isdigit() for char in v):
            raise ValueError("Password must contain at least one digit")

        if not any(char.isupper() for char in v):
            raise ValueError("Password must contain at least one uppercase letter")

        if not any(char.islower() for char in v):
            raise ValueError("Password must contain at least one lowercase letter")

        if not any(char in "!@#$%^&*()_+" for char in v):
            raise ValueError("Password must contain at least one special character")
        

    def __repr__(self):
        return f'Password({super().__repr__()})'

@dataclass(frozen=True)
class Post(str, ValueObject, Enum):
    BACKEND = 'backend'
    FRONTEND = 'frontend'
    DESIGNER = 'designer'
    MANAGER = 'manager'
        

    def __repr__(self):
        return f'Post({super().__repr__()})'


