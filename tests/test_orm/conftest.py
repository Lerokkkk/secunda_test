import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.building import Building
from domain.value_objects.building import Coordinates


@pytest_asyncio.fixture
async def building(session: AsyncSession) -> Building:
    building = Building(
        address="ул. Ленина 1",
        location=Coordinates(latitude=55.75, longitude=37.61),
    )

    session.add(building)
    await session.flush()
    return building
    
    