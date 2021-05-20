from source.domain import command
from source.domain import model
from datetime import date

def add_product(cmd: command.AddProduct) -> model.Product:
    return model.product_factory(
        id_=cmd.id_,
        name=cmd.name,
        purchase_price=cmd.purchase_price,
        sales_price=cmd.sales_price,
        brand_id=cmd.brand_id,
        category_id=cmd.category_id,
        type_id=cmd.type_id,
        quantity=cmd.quantity,
        description=cmd.description,
        rating_id=cmd.rating_id,
        active=cmd.active
    )


def update_product(cmd: command.UpdateProductCommand) -> model.Product:
    if isinstance(cmd, command.UpdateProduct):
        return cmd.product.update({
            'name': cmd.name,
            'purchase_price': cmd.purchase_price,
            'sales_price': cmd.sales_price,
            'brand_id': cmd.brand_id,
            'category_id': cmd.category_id,
            'type_id': cmd.type_id,
            'quantity': cmd.quantity,
            'description': cmd.description,
            'rating_id': cmd.rating_id,
            'active': cmd.active


        })
    if isinstance(cmd, command.UpdateProductName):
        return cmd.product.update({
            'name': str
        })
    elif isinstance(cmd, command.UpdateProductSalesPrice):
        return cmd.product.update({
            'sales_price': float
        })
    elif isinstance(cmd, command.UpdateProductPurchasePrice):
        return cmd.product.update({
            'purchase_price': float
        })
    elif isinstance(cmd, command.UpdateProductQuantity):
        return cmd.product.update({
            'quantity': int
        })
