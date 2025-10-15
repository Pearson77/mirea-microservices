from src.repositories.items_repository import ItemsRepository


class ItemsService:
    def __init__(
            self,
            repository: ItemsRepository,
    ):
        self.repository = repository

    async def create_item(self):
        ...

    async def get_items(self):
        ...

    async def delete_item(self, item_id: int):
        ...