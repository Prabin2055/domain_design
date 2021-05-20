import abc
from source.domain import model
from typing import Set


class AbstractRepository(abc.ABC):
    def __init__(self):
        self.seen=set()

    @abc.abstractmethod
    async def get(self, id_):
        raise NotImplementedError

    @abc.abstractmethod
    async def add(self, model=None):
        raise NotImplementedError

    @abc.abstractmethod
    async def update(self, id_=None, model=None) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    async def delete(self, id_=None, model=None):
        raise NotImplementedError


    # def add(self,product:model.Product):
    #     self._add(product)
    #     self.seen.add(product)
    #     print("seen",self.seen)

    # def get(self, id_) -> model.Product:  #(3)
    #     product = self._get(id_)
    #     if product:
    #         self.seen.add(product)
    #     return product

    # @abc.abstractmethod
    # def _add(self, product:model.Product):
    #     raise NotImplementedError

    # @abc.abstractmethod
    # def _get(self, id_=None) -> model.Product :
    #     raise NotImplemented