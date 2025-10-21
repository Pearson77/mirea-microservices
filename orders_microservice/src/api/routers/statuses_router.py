from fastapi import APIRouter, Depends, HTTPException

from src.api.dependencies import get_statuses_service
from src.services.statuses_service import StatusesService

router = APIRouter(
    prefix="/statuses",
    tags=["Statuses"]
)


@router.post("")
async def create_status(
        title: str,
        service: StatusesService = Depends(get_statuses_service),
):
    return await service.create_status(title)


@router.get("")
async def get_statuses(
        service: StatusesService = Depends(get_statuses_service),
):
    return await service.get_statuses()


@router.delete("/{status_id}")
async def delete_status(
        status_id: int,
        service: StatusesService = Depends(get_statuses_service),
):
    if result := await service.delete_status(status_id):
        return result
    raise HTTPException(status_code=404, detail="Status not found")