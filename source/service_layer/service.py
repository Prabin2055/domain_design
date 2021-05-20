from __future__ import annotations
from source.domain import command
from source.service_layer import abstract, handlers
from source.adapters.repository import ProductRepository
from uuid import UUID
from source.domain import events
from source.service_layer import unit_of_work


async def add_product(validated_data: abstract.AddProduct, uow: unit_of_work.ProductUnitOfWork, event:events.ProductCreated) -> None:
    with uow() as w:
        product = handlers.add_product(
            command.AddProduct(
                id_=validated_data.id_,
                name=validated_data.name,
                purchase_price=validated_data.purchase_price,
                sales_price=validated_data.sales_price,
                brand_id=validated_data.brand_id,
                category_id=validated_data.category_id,
                type_id=validated_data.type_id,
                quantity=validated_data.quantity,
                description=validated_data.description,
                rating_id=validated_data.rating_id,
                active=validated_data.active,
            )
        )
        # repo = ProductRepository()
        # repo.add(product)
        # uow.commit()
        w.storedata = product
        w.commit()


async def update_product(id_:int, validated_data: abstract.UpdateProduct, uow: unit_of_work.ProductUnitOfWork, event:events.ProductUpdated) -> None:
    with uow() as w:
        repo = ProductRepository()
        product = w.repo.get(id_)
        product_ = handlers.update_product(command.UpdateProduct(
            product=product,
            name=validated_data.name if validated_data.name else product.name,
            purchase_price=validated_data.purchase_price if validated_data.purchase_price else product.purchase_price,
            sales_price=validated_data.sales_price if validated_data.sales_price else product.sales_price,
            brand_id=validated_data.brand_id if validated_data.brand_id else product.brand_id,
            category_id=validated_data.category_id if validated_data.category_id else product.category_id,
            type_id=validated_data.type_id if validated_data.type_id else product.type_id,
            quantity=validated_data.quantity if validated_data.quantity else product.quantity,
            description=validated_data.description if validated_data.description else product.description,
            rating_id=validated_data.rating_id if validated_data.rating_id else product.rating_id,
            active=validated_data.active if validated_data.active else product.active

        ))
        # repo.update(id_, product_)
        # uow.commit()
        w.id_=id_
        w.storeDataUpdate = product_
        w.commit()


def update_product_name(id_: UUID, validated_data: abstract.UpdateProductName):
    repo = ProductRepository()
    product = repo.get(id_)
    product = handlers.update_product(
        command.UpdateProductName(product=product, name=validated_data.name)
    )
    repo.update(product)


def update_product_sales_price(
    id_: UUID, validated_data: abstract.UpdateProductSalesPrice
):
    repo = ProductRepository()
    product = repo.get(id_)
    product = handlers.update_product(
        command.UpdateProductSalesPrice(
            product=product, sales_price=validated_data.sales_price
        )
    )
    repo.update(product)


def update_product_purchase_price(
    id_: UUID, validated_data: abstract.UpdateProductPurchasePrice
):
    repo = ProductRepository()
    product = repo.get(id_)
    product = handlers.update_product(
        command.UpdateProductPurchasePrice(
            product=product, purchase_price=validated_data.purchase_price
        )
    )
    repo.update(product)


def update_product_quantity(id_: UUID, validated_data: abstract.UpdateProductQuantity):
    repo = ProductRepository()
    product = repo.get(id_)
    product = handlers.update_product(
        command.UpdateProductQuantity(
            product=product, quantity=validated_data.quantity)
    )
    repo.update(product)
