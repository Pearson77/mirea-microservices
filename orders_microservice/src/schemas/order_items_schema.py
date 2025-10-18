from pydantic import BaseModel


class AddItemSchema(BaseModel):
    item_id: int
    order_id: int


class RemoveItemSchema(BaseModel):
    item_id: int

