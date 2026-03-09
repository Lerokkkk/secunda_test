from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.activity import Activity
from domain.entities.building import Building
from domain.entities.organization import Organization
from domain.value_objects.building import Coordinates
from domain.value_objects.organization import PhoneNumber


async def test_building_mapper(session: AsyncSession, building: Building):
    oid = building.oid
    session.expire_all()

    res = await session.get(Building, oid)

    print(res)
    assert res.oid == oid
    assert res.address == building.address
    assert res.location == building.location
    assert isinstance(res.location, Coordinates)
    assert isinstance(res, Building)


async def test_activity_mapper(session: AsyncSession):
    activity = Activity.create(title="Еда", parent=None)
    session.add(activity)
    await session.flush()
    oid = activity.oid

    session.expire_all()

    res = await session.get(Activity, oid)

    assert res.oid == oid
    assert res.title == "Еда"
    assert res.level == 1
    assert res.parent_id is None
    assert isinstance(res, Activity)


async def test_activity_mapper_with_parent(session: AsyncSession):
    parent = Activity.create(title="Еда", parent=None)
    child = Activity.create(title="Мясо", parent=parent)

    session.add(parent)
    session.add(child)
    await session.flush()
    
    child_oid = child.oid
    parent_oid = parent.oid 
    
    session.expire_all()

    res = await session.get(Activity, child_oid)

    assert res.title == "Мясо"
    assert res.level == 2
    assert res.parent_id == parent_oid

async def test_organization_mapper(session: AsyncSession, building: Building):
    building_oid = building.oid
    
    org = Organization(
        title="Рога и Копыта",
        phone=[PhoneNumber(value="+79991234567"), PhoneNumber(value="+79997654321")],
        building_id=building_oid,
    )
    session.add(org)
    await session.flush()
    oid = org.oid

    session.expire_all()

    res = await session.get(Organization, oid)

    assert res.oid == oid
    assert res.title == "Рога и Копыта"
    assert res.building_id == building_oid
    assert len(res.phone) == 2
    assert all(isinstance(p, PhoneNumber) for p in res.phone)
    assert {p.value for p in res.phone} == {"+79991234567", "+79997654321"}