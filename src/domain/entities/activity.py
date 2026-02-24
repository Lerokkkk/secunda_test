from dataclasses import dataclass, field
from uuid import UUID, uuid4

from domain.entities.base import Entity
from domain.exceptions.activity import ActivityHierarchyTooDeep


@dataclass
class Activity(Entity):
    title: str
    level: int
    parent_id: UUID | None = field(default=None)

    @classmethod
    def create(cls, title: str, parent: "Activity | None") -> "Activity":
        if parent and parent.level >= 3:
            raise ActivityHierarchyTooDeep(parent.level)
        return cls(
            title=title, parent_id=parent.oid, level=(parent.level + 1) if parent else 1
        )