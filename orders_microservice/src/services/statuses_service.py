from src.repositories.statuses_repository import StatusesRepository


class StatusesService:
    def __init__(
            self,
            repository: StatusesRepository,
    ):
        self.repository = repository

    async def get_statuses(self):
        return await self.repository.read_statuses()

    async def create_status(self, title: str):
        return await self.repository.create_status(title)

    async def delete_status(self, status_id: int):
        return await self.repository.delete_status(status_id)