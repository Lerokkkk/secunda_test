from infra.gateway.postgres.alchemy.base import mapper_registry
from uuid import uuid4
import sqlalchemy as sa


ORGANIZATION_TABLE = sa.Table(
    "organizations",
    mapper_registry.metadata,
    sa.Column("id", sa.UUID(as_uuid=True), primary_key=True, default=uuid4),
    sa.Column("title", sa.String, nullable=False),
    sa.Column(
        "building_id",
        sa.UUID(as_uuid=True),
        sa.ForeignKey("buildings.id", ondelete="SET NULL"),
        nullable=True,
    ),
)

ORGANIZATION_PHONES_TABLE = sa.Table(
    "organization_phones",
    mapper_registry.metadata,
    sa.Column("id", sa.UUID(as_uuid=True), primary_key=True, default=uuid4),
    sa.Column(
        "organization_id",
        sa.UUID(as_uuid=True),
        sa.ForeignKey("organizations.id", ondelete="CASCADE"),
        nullable=False,
    ),
    sa.Column("phone", sa.String, nullable=False),
)

ORGANIZATION_ACTIVITY_TABLE = sa.Table(
    "organization_activities",
    mapper_registry.metadata,
    sa.Column(
        "organization_id",
        sa.UUID(as_uuid=True),
        sa.ForeignKey("organizations.id", ondelete="CASCADE"),
        nullable=False,
    ),
    sa.Column(
        "activity_id",
        sa.UUID(as_uuid=True),
        sa.ForeignKey("activities.id", ondelete="CASCADE"),
        nullable=False,
    ),
)
