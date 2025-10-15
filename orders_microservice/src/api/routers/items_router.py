from fastapi import APIRouter, Depends

from src.api.dependencies import get_items_service
from src.services.items_service import ItemsService

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)


@router.post("")
async def create_item(
        service: ItemsService = Depends(get_items_service),
):
    ...


@router.get("")
async def get_items(
        service: ItemsService = Depends(get_items_service),
):
    ...


@router.delete("/{item_id}")
async def delete_item(
        item_id: int,
        service: ItemsService = Depends(get_items_service),
):
    ...