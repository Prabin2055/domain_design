from pydantic import BaseModel
from datetime import date
from uuid import UUID
from source.domain import model


class AddProduct(BaseModel):
    id_: UUID
    name: str
    purchase_price: float
    sales_price: float
    brand_id: str
    category_id: str
    type_id: str
    quantity: int
    description: str
    rating_id: str
    active: bool


class UpdateProductCommand(BaseModel):
    product: model.Product


class UpdateProduct(UpdateProductCommand):
    name: str
    purchase_price: float
    sales_price: float
    brand_id: str
    category_id: str
    type_id: str
    quantity: int
    description: str
    rating_id: str
    active: bool


class UpdateProductName(UpdateProductCommand):
    name: str


class UpdateProductSalesPrice(UpdateProductCommand):
    sales_price: float


class UpdateProductPurchasePrice(UpdateProductCommand):
    purchase_price: float


class UpdateProductQuantity(UpdateProductCommand):
    quantity: int
