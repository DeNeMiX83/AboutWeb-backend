from sqlalchemy import (
    Column, String, Enum, ForeignKey
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import composite, relationship
import uuid

from app.infrastructure.db.sqlalchemy.models import Base

from app.core.user import entities
from app.core.user.entities import value_objects as vo


class User(Base):
    __tablename__ = 'users'

    _id = Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    _username = Column("username", String, nullable=False)
    _email = Column("email", String, nullable=False, unique=True)
    _hashed_password = Column("hashed_password", String, nullable=False)
    avatar_id = Column(
        UUID(as_uuid=True), ForeignKey("images.id", ondelete="CASCADE"),
        nullable=False,
    )

    id = composite(vo.UserID, _id)
    username = composite(vo.UserName, _username)
    email = composite(vo.Email, _email)
    hashed_password = composite(vo.HashedPassword, _hashed_password)
    avatar = relationship("Image", back_populates="user")
    positions = relationship("UserPositions", back_populates="user")


class UserPositions(Base):
    __tablename__ = 'user_positions'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )
    post_id = Column(
        UUID(as_uuid=True), ForeignKey("positions.id", ondelete="CASCADE"),
        nullable=False
    )

    user = relationship("User", back_populates="positions")


class Position(Base):
    __tablename__ = 'positions'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(Enum(vo.Position))


def user_mapping(mapper_registry):
    table = User.__table__
    mapper_registry.map_imperatively(
        entities.User, table,
        relationships={
            "avatar": relationship(
                "Image", back_populates="user",
                cascade="all, delete-orphan",
            ),
            "positions": relationship(
                "UserPositions", back_populates="user",
                cascade="all, delete-orphan",
            ),
        },
    )
