from infra.gateway.postgres.alchemy.base import mapper_registry
from uuid import uuid4
import sqlalchemy as sa

from geoalchemy2 import Geography


BUILDING_TABLE = sa.Table(
    "buildings",
    mapper_registry.metadata,
    sa.Column("id", sa.UUID(as_uuid=True), primary_key=True, default=uuid4),
    sa.Column("address", sa.String, unique=True, nullable=False),
    sa.Column("location", Geography(geometry_type="POINT", srid=4326), nullable=False),
)
