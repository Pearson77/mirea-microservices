from fastapi import APIRouter, Depends

from src.api.dependencies import get_orders_service
from src.services.orders_service import OrdersService

router = APIRouter(
    prefix="/statuses",
    tags=["Statuses"]
)


@router.post("")
async def create_status(
        title: str,
        service: OrdersService = Depends(get_orders_service),
):
    return await service.create_status(title)


@router.get("")
async def get_statuses(
        service: OrdersService = Depends(get_orders_service),
):
    return await service.get_statuses()


@router.delete("/{status_id}")
async def delete_status(
        status_id: int,
        service: OrdersService = Depends(get_orders_service),
):
    return await service.delete_status(status_id)