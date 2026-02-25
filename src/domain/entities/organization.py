from dataclasses import dataclass, field
import uuid

from domain.entities.base import Entity
from domain.value_objects.organization import PhoneNumber


@dataclass
class Organization(Entity):
    title: str
    phone: list[PhoneNumber]
    building_id: uuid.UUID
    activity_ids: list[uuid.UUID] = field(default_factory=list)
