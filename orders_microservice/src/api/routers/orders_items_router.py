from fastapi import APIRouter, Depends, Body

from src.api.dependencies import get_orders_items_service
from src.services.orders_items_service import OrdersItemsService

router = APIRouter(
    prefix="/order-items",
    tags=["OrderItems"]
)


@router.post("")
async def add_item_to_order(
        service: OrdersItemsService = Depends(get_orders_items_service),
):
    ...


@router.get("/{order_id}")
async def get_order_items(
        order_id: int,
        service: OrdersItemsService = Depends(get_orders_items_service),
):
    ...


@router.delete("/{order_id}")
async def remove_item_from_order(
        order_id: int,
        item_id: int = Body(..., title="item id"),
        service: OrdersItemsService = Depends(get_orders_items_service),
):
    ...