from src.repositories.items_repository import ItemsRepository
from src.repositories.orders_items_repository import OrderItemsRepository
from src.repositories.orders_repository import OrdersRepository
from src.repositories.statuses_repository import StatusesRepository
from src.services.orders_service import OrdersService


async def get_orders_service() -> OrdersService:
    return OrdersService(OrdersRepository(), OrderItemsRepository(), ItemsRepository(), StatusesRepository())