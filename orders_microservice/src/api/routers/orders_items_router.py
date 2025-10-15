from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/order-items",
    tags=["OrderItems"]
)


@router.post("")
async def add_item_to_order():
    ...


@router.get("/{order_id}")
async def get_order_items(order_id: int):
    ...


@router.delete("/{order_id}/item/{item_id}")
async def remove_item_from_order(order_id: int, item_id: int):
    ...