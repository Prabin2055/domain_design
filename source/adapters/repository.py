from source.domain import model
import os
import pickle
from source.adapters import abstractrepo
from uuid import UUID
database = {}
i = 0


class ProductRepository(abstractrepo.AbstractRepository):
    def get(self, id_: int) -> model.Product:
        data = database[id_]
        print("GET, data", data)
        product_data = model.Product(**data)
        return product_data

    def add(self, model: model.Product):
        values = {
            "id_": model.id_,
            "name": model.name,
            "purchase_price": model.purchase_price,
            "sales_price": model.sales_price,
            "brand_id": model.brand_id,
            "category_id": model.category_id,
            "type_id": model.type_id,
            "quantity": model.quantity,
            "description": model.description,
            "rating_id": model.rating_id,
            "active": model.active,
        }
        # await model.append(values)
        global i
        i += 1
        database[i] = values
        with open('database.pickle', 'wb') as handle:
            pickle.dump(database, handle, protocol=pickle.HIGHEST_PROTOCOL)
        print(database)

    def update(self, id_, model: model.Product) -> None:
        values = {
            "id_": model.id_,
            "name": model.name,
            "purchase_price": model.purchase_price,
            "sales_price": model.sales_price,
            "brand_id": model.brand_id,
            "category_id": model.category_id,
            "type_id": model.type_id,
            "quantity": model.quantity,
            "description": model.description,
            "rating_id": model.rating_id,
            "active": model.active,
        }
        database[id_] = values
        print(database)

    async def delete(self, id_, model: model.Product) -> None:
        if self.id_ in model.id_:
            del model[id_]
