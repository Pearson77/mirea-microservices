from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/statuses",
    tags=["Statuses"]
)


@router.post("")
async def create_status():
    ...


@router.get("")
async def get_statuses():
    ...


@router.delete("/{status_id}")
async def delete_status(status_id: int):
    ...