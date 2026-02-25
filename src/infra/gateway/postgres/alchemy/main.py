import asyncio

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from infra.gateway.postgres.alchemy.base import mapper_registry
import infra.gateway.postgres.alchemy  # noqa F401
from project.settings import Settings

engine = create_async_engine(Settings().pg_dsn, echo=True)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# async def get_session() -> AsyncGenerator[AsyncSession]:
#     async with async_session() as session:
#         yield session


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(mapper_registry.metadata.create_all)
    print("TAbles created")
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
