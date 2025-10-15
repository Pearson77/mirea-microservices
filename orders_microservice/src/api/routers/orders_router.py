from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("")
async def create_order():
    ...


@router.get("")
async def get_orders():
    ...


@router.get("/{order_id}")
async def get_order(order_id: int):
    ...


@router.put("/{order_id}")
async def update_order(order_id: int):
    ...


@router.delete("/{order_id}")
async def delete_order(order_id: int):
    ...