from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)