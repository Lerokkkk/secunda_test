import asyncio
import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


from infra.gateway.postgres.alchemy.base import mapper_registry
from infra.gateway.postgres.alchemy import * # noqa 403
from project.settings import Settings


@pytest.fixture(scope="session", autouse=True)
def settings() -> Settings:
    return Settings()

@pytest_asyncio.fixture(scope="session", autouse=True)
async def engine(settings: Settings):
    engine = create_async_engine(settings.test_pg_dsn, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(mapper_registry.metadata.create_all)
    yield engine
    async with engine.begin() as conn:
        await conn.run_sync(mapper_registry.metadata.drop_all)
    await engine.dispose()


@pytest_asyncio.fixture
async def session(engine):
    async_session = async_sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
        await session.rollback()

