from domain.entities.building import Building
from domain.value_objects.building import Coordinates
from .base import mapper_registry
from uuid import uuid4
import sqlalchemy as sa

from geoalchemy2 import Geography
from geoalchemy2.shape import from_shape, to_shape
from shapely import Point


class CoordinatesType(sa.TypeDecorator):
    impl = Geography("POINT", srid=4326)
    cache_ok = True

    def process_bind_param(self, value: Coordinates | None, dialect):
        if value is None:
            return None
        return from_shape(Point(value.longitude, value.latitude), srid=4326)
    
    def process_result_value(self, value, dialect) -> Coordinates | None:
        if value is None:
            return None
        point = to_shape(value)
        return Coordinates(latitude=point.y, longitude=point.x)


BUILDING_TABLE = sa.Table(
    "buildings",
    mapper_registry.metadata,
    sa.Column("id", sa.UUID(as_uuid=True), primary_key=True, default=uuid4),
    sa.Column("address", sa.String, unique=True, nullable=False),
    sa.Column("location", CoordinatesType(), nullable=False),
)

mapper_registry.map_imperatively(
    Building, BUILDING_TABLE, properties={"oid": BUILDING_TABLE.c.id}
)
