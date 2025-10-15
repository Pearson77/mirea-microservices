from fastapi import APIRouter, Depends

from src.api.dependencies import get_orders_service
from src.schemas.orders_schemas import OrderUpdateSchema, OrderCreateSchema
from src.services.orders_service import OrdersService

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("")
async def create_order(
        new_order: OrderCreateSchema,
        service: OrdersService = Depends(get_orders_service),
):
    return await service.create_order(new_order)


@router.get("")
async def get_orders(
        service: OrdersService = Depends(get_orders_service),
):
    return await service.get_orders()


@router.get("/{order_id}")
async def get_order(
        order_id: int,
        service: OrdersService = Depends(get_orders_service),
):
    return await service.get_order(order_id)


@router.patch("/{order_id}")
async def update_order(
        order_id: int,
        new_order: OrderUpdateSchema,
        service: OrdersService = Depends(get_orders_service),
):
    return await service.update_order(order_id, new_order)


@router.delete("/{order_id}")
async def delete_order(
        order_id: int,
        service: OrdersService = Depends(get_orders_service),
):
    return await service.delete_order(order_id)