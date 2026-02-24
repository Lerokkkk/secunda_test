from domain.exceptions.building import LatitudeException, LongitudeException
from domain.value_objects.base import BaseValueObject


class Coordinates(BaseValueObject):
    latitude: float
    longitude: float

    def _validate(self) -> None:
        if not (-90 <= self.latitude <= 90):
            raise LatitudeException(self.latitude)
        if not (-180 <= self.longitude <= 180):
            raise LongitudeException(self.longitude)
