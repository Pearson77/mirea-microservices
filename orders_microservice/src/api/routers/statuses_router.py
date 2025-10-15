from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/statuses",
    tags=["Statuses"]
)


@router.get("/statuses")
async def get_statuses():
    ...