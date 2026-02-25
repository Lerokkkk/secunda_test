# tests/test_orm.py
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.building import Building
from domain.value_objects.building import Coordinates


async def test_building_mapper(session: AsyncSession):
    building = Building(
        address="ул. Ленина 1",
        location=Coordinates(latitude=55.75, longitude=37.61),
    )
    res = (await session.execute(text("SELECT * FROM buildings"))).all()
    print(res)
