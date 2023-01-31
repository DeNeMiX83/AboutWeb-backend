from app.infrastructure.db.sqlalchemy.models import (
    user_mapping
)
from app.infrastructure.db.sqlalchemy.models import Base


def start_mappers():
    mapper_registry = Base.registry
    user_mapping(mapper_registry)