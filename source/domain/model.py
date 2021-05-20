from dataclasses import dataclass
from pydantic import BaseModel
from datetime import date
from uuid import UUID
from typing import Dict, Any, List, Optional
from source.domain.events import Event


class Product(BaseModel):
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
    # event: List[Event]=None
    events:Optional[List]

    class Config:
        allow_mutation = False
        extra = "forbid"
        title = "Product"
        arbitrary_types_allowed = True

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))

    def update(self, mapping: Dict[str, Any]):
        return self.copy(update=mapping)

    def product_updated():
        pass


def product_factory(
    id_: UUID,
    name: str,
    purchase_price: float,
    sales_price: float,
    brand_id: str,
    category_id: str,
    type_id: str,
    quantity: int,
    description: str,
    rating_id: str,
    active: bool,

) -> Product:
    return Product(
        id_=id_,
        name=name,
        purchase_price=purchase_price,
        sales_price=sales_price,
        brand_id=brand_id,
        category_id=category_id,
        type_id=type_id,
        quantity=quantity,
        description=description,
        rating_id=rating_id,
        active=active,
        events=[]
    )


class Order(BaseModel):
    order_id: UUID
    customer_id: UUID
    order_date: date
    order_amount: float
    discount: float
    shipping_amount: float
    tax_amount: float
    net_amount: float
    shipping_date: date
    shipping_address_id: str
    billing_address_id: str
    status_id: bool

    class Config:
        allow_mutation = False
        extra = "forbid"
        title = "Order"

    def update(self, mapping: Dict[str, Any]):
        return self.copy(update=mapping)


def order_factory(
    order_id: UUID,
    customer_id: UUID,
    order_date: date,
    order_amount: float,
    discount: float,
    shipping_amount: float,
    tax_amount: float,
    net_amount: float,
    shipping_date: date,
    shipping_address_id: str,
    billing_address_id: str,
    status_id: bool,
) -> Order:
    return Order(
        order_id=order_id,
        customer_id=customer_id,
        order_date=order_date,
        order_amount=order_amount,
        discount=discount,
        shipping_amount=shipping_amount,
        tax_amount=tax_amount,
        net_amount=net_amount,
        shipping_date=shipping_date,
        shipping_address_id=shipping_address_id,
        billing_address_id=billing_address_id,
        status_id=status_id,
    )
