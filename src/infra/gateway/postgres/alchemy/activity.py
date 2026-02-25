from domain.entities.activity import Activity
from .base import mapper_registry
from uuid import uuid4
import sqlalchemy as sa

ACTIVITY_TABLE = sa.Table(
    "activities",
    mapper_registry.metadata,
    sa.Column("id", sa.UUID(as_uuid=True), primary_key=True, default=uuid4),
    sa.Column("title", sa.String, nullable=False),
    sa.Column("level", sa.Integer, nullable=False),
    sa.Column(
        "parent_id",
        sa.UUID(as_uuid=True),
        sa.ForeignKey("activities.id", ondelete="CASCADE"),
        nullable=True,
    ),
)

mapper_registry.map_imperatively(
    Activity,
    ACTIVITY_TABLE,
    properties={
        "oid": ACTIVITY_TABLE.c.id,
    }
)