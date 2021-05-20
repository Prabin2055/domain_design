from source.domain.events import Event
from uuid import UUID
from sanic import Sanic, response
from sanic.response import text, json
from source.domain import events
from sanic.response import HTTPResponse
from source.service_layer import service, unit_of_work, abstract
import asyncio

app = Sanic(__name__)


@app.get("/")
async def hello_world(request):
    return text("hello")


@app.route("/product", methods=["GET", "POST"])
async def add_product(request):
    await service.add_product(
        validated_data=abstract.AddProduct(
            id_="cf57432e-809e-4353-adbd-9d5c0d733868",
            name="Lenovo",
            purchase_price="123.33",
            sales_price="234",
            brand_id="lp",
            category_id="El",
            type_id="dell",
            quantity=3,
            description="best new model",
            rating_id="md",
            active=True
        ), uow=unit_of_work.ProductUnitOfWork, event=events.ProductCreated
    )
    return HTTPResponse("successfully Added")


@app.route("/update", methods=['GET', 'POST'])
async def update_product(request):
    await service.update_product(id_=1, validated_data=abstract.UpdateProduct(
        name="Dell"
    ), uow=unit_of_work.UpdateProductUnitOfWork, event=events.ProductUpdated)
    return HTTPResponse("success")

if __name__ == "__main__":
    asyncio.run(app(auto_reload=True, debug=True, workers=4))
    # app.run(auto_reload=True, debug=True, workers=4)
