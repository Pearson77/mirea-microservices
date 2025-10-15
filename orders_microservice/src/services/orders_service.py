from sqlalchemy.testing.pickleable import Order

from src.repositories.items_repository import ItemsRepository
from src.repositories.orders_items_repository import OrderItemsRepository
from src.repositories.orders_repository import OrdersRepository
from src.repositories.statuses_repository import StatusesRepository


class OrdersService:
    def __init__(
            self,
            repository: OrdersRepository,
    ):
        self.repository = repository

    async def get_orders(self):
        ...

    async def get_order(self, order_id: int):
        ...

    async def create_order(self):
        ...

    async def update_order(self, order_id: int):
        ...

    async def delete_order(self, order_id: int):
        ...