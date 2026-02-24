from dataclasses import dataclass

from domain.exceptions.base import BaseDomainException


@dataclass(eq=False)
class NumberParseException(BaseDomainException):
    phone: str

    @property
    def message(self) -> str:
        return f"{self.phone} is not valid phone number"
