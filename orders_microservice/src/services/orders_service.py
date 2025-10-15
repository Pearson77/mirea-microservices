from src.repositories.items_repository import ItemsRepository
from src.repositories.orders_items_repository import OrderItemsRepository
from src.repositories.orders_repository import OrdersRepository
from src.repositories.statuses_repository import StatusesRepository


class OrdersService:
    def __init__(
            self,
            orders_repo: OrdersRepository,
            order_items_repo: OrderItemsRepository,
            items_repo: ItemsRepository,
            statuses_repo: StatusesRepository,
    ):
        self.orders_repo = orders_repo
        self.order_items_repo = order_items_repo
        self.items_repo = items_repo
        self.statuses_repo = statuses_repo

    # Заказы

    # Товары заказа

    # Товары

    async def get_statuses(self):
        return await self.statuses_repo.read_statuses()

    async def create_status(self, title: str):
        return await self.statuses_repo.create_status(title)

    async def delete_status(self, status_id: int):
        return await self.statuses_repo.delete_status(status_id)