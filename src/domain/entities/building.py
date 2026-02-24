from dataclasses import dataclass, field
from uuid import UUID, uuid4

from domain.entities.base import Entity
from domain.value_objects.building import Coordinates

@dataclass
class Building(Entity):
    address: str
    location: Coordinates