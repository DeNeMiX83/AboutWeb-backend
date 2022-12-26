from dataclasses import dataclass
import uuid
from app.core.shared.entities.value_objects import UUID

@dataclass()
class Entity():
    id: UUID

    @classmethod
    def generate_id(cls) -> UUID:
        return uuid.uuid4()