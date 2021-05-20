from dataclasses import dataclass
from uuid import UUID


class Event:
    pass


@dataclass
class ProductCreated(Event):
    id_: UUID
    # name: str
    # purchase_price: float
    # sales_price: float
    # brand_id: str
    # category_id: str
    # type_id: str
    # quantity: int
    # description: str
    # rating_id: str
    # active: bool


@dataclass
class ProductUpdated(Event):
    id_: UUID
    name: str
