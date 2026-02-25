from dataclasses import dataclass
from uuid import UUID
import phonenumbers

from domain.exceptions.organization import NumberParseException
from domain.value_objects.base import BaseValueObject, ValueObject


@dataclass(frozen=True)
class PhoneNumber(ValueObject[str]):
    value: str

    def _validate(self) -> None:
        try:
            phonenumbers.parse(self.value)
        except phonenumbers.NumberParseException:
            raise NumberParseException(self.value)
