from pydantic import BaseModel
from uuid import UUID
from datetime import date
from typing import Optional


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


class UpdateProduct(BaseModel):
    id_:Optional[UUID]=None
    name: Optional[str] = None
    purchase_price: Optional[float] = None
    sales_price: Optional[float] = None
    brand_id: Optional[str] = None
    category_id: Optional[str] = None
    type_id: Optional[str] = None
    quantity: Optional[int] = None
    description: Optional[str] = None
    rating_id: Optional[str] = None
    active: Optional[str] = None


class UpdateProductName(BaseModel):
    name: str


class UpdateProductSalesPrice(BaseModel):
    sales_price: float


class UpdateProductPurchasePrice(BaseModel):
    purchase_price: float


class UpdateProductQuantity(BaseModel):
    quantity: int
