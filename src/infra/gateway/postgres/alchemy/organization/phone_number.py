from domain.value_objects.organization import PhoneNumber
from ..base import mapper_registry
from uuid import uuid4
import sqlalchemy as sa

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

mapper_registry.map_imperatively(
    PhoneNumber,
    ORGANIZATION_PHONES_TABLE,
    properties={
        "value": ORGANIZATION_PHONES_TABLE.c.phone,
    },
)