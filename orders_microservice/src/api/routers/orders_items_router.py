from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/order-items",
    tags=["OrderItems"]
)