from src.repositories.items_repository import ItemsRepository
from src.repositories.orders_items_repository import OrdersItemsRepository
from src.repositories.orders_repository import OrdersRepository
from src.repositories.statuses_repository import StatusesRepository
from src.schemas.orders_schemas import OrderCreateSchema, OrderUpdateSchema


class OrdersService:
    def __init__(
            self,
            repository: OrdersRepository,
    ):
        self.repository = repository

    async def get_orders(self):
        return await self.repository.get_orders()

    async def get_order(self, order_id: int):
        return await self.repository.get_order(order_id)

    async def create_order(self, new_order: OrderCreateSchema):
        return await self.repository.create_order(new_order)

    async def update_order(self, order_id: int, new_order: OrderUpdateSchema):
        return await self.repository.update_order(order_id, new_order)

    async def delete_order(self, order_id: int):
        return await self.repository.delete_order(order_id)