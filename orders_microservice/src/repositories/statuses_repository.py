from sqlalchemy import select, insert, delete

from src.database.connection import async_session_maker
from src.database.models import Statuses


class StatusesRepository:

    @staticmethod
    async def create_status(title: str):
        async with async_session_maker() as session:
            result = await session.execute(
                insert(Statuses)
                .values(title=title)
                .returning(Statuses)
            )
            await session.commit()
            return result.scalar_one_or_none()

    @staticmethod
    async def read_statuses():
        async with async_session_maker() as session:
            result = await session.execute(
                select(Statuses)
            )
            await session.commit()
            return result.scalars().all()

    @staticmethod
    async def delete_status(status_id: int):
        async with async_session_maker() as session:
            result = await session.execute(
                delete(Statuses)
                .where(Statuses.id == status_id)
                .returning(Statuses)
            )
            await session.commit()
            return result.scalar_one_or_none()