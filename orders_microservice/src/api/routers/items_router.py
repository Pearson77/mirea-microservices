from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)


@router.post("")
async def create_item():
    ...


@router.get("")
async def get_items():
    ...


@router.delete("/{item_id}")
async def delete_item(item_id: int):
    ...