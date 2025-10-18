from src.repositories.items_repository import ItemsRepository
from src.repositories.orders_items_repository import OrdersItemsRepository
from src.repositories.orders_repository import OrdersRepository
from src.repositories.statuses_repository import StatusesRepository
from src.services.items_service import ItemsService
from src.services.orders_service import OrdersService
from src.services.statuses_service import StatusesService


async def get_orders_service() -> OrdersService:
    return OrdersService(OrdersRepository(), OrdersItemsRepository())


async def get_items_service() -> ItemsService:
    return ItemsService(ItemsRepository())


async def get_statuses_service() -> StatusesService:
    return StatusesService(StatusesRepository())