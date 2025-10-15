from fastapi import APIRouter

from src.api.routers.orders_router import router as orders_router
from src.api.routers.orders_items_router import router as orders_items_router
from src.api.routers.items_router import router as items_router
from src.api.routers.statuses_router import router as statuses_router

base_router = APIRouter()

base_router.include_router(orders_router)
base_router.include_router(orders_items_router)
base_router.include_router(items_router)
base_router.include_router(statuses_router)