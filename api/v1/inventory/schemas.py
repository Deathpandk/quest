from app.utils.schemas import BaseSchema


class CreateInventoryChangeRequest(BaseSchema):
    product_variation_id: str
    change: int
