from src.repositories.orders_items_repository import OrdersItemsRepository


class OrdersItemsService:
    def __init__(
            self,
            repository: OrdersItemsRepository,
    ):
        self.repository = repository