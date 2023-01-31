from dataclasses import dataclass
import uuid
from uuid import UUID

@dataclass()
class Entity():
    id: UUID

    @classmethod
    def generate_id(cls) -> UUID:
        return uuid.uuid4()