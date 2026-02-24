from dataclasses import dataclass

from domain.exceptions.base import BaseDomainException


@dataclass(eq=False)
class LatitudeException(BaseDomainException):
    latitude: float

    @property
    def message(self) -> str:
        return f"Latitude must be between -90 and 90, your: {self.latitude}"


@dataclass(eq=False)
class LongitudeException(BaseDomainException):
    longitude: float

    @property
    def message(self) -> str:
        return f"Longitude must be between -180 and 180, your: {self.longitude}"
