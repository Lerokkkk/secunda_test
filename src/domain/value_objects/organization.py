import phonenumbers
from domain.exceptions.activity import NumberParseException
from domain.value_objects.base import ValueObject


class PhoneNumber(ValueObject[str]):
    value: str

    def _validate(self) -> None:
        try:
            phonenumbers.parse(self.value)
        except phonenumbers.NumberParseException:
            raise NumberParseException(self.value)
