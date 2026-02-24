from dataclasses import dataclass

from domain.exceptions.base import BaseDomainException


@dataclass(eq=False)
class ActivityHierarchyTooDeep(BaseDomainException):
    a_level: int

    @property
    def message(self) -> str:
        return f"Activity nesting level {self.a_level} exceeds the allowed maximum"
