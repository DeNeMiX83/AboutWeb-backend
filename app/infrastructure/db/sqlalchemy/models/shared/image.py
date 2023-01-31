from sqlalchemy import (
    Column, String, Enum
)
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.infrastructure.db.sqlalchemy.models import Base


class Image(Base):
    __tablename__ = 'images'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    path = Column("path", String, nullable=False)