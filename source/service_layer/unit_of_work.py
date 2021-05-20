
from __future__ import annotations
import abc
from source.adapters.repository import ProductRepository
from source.service_layer.abstractunitofwork import AbstractUnitOfWork
from source.service_layer import messagebus
from source.domain import events


class ProductUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.repo = ProductRepository()

    def __enter__(self):
        self.storeData = None
        return self

    def __exit__(self, *args):
        return super().__exit__(*args)

    def commit(self):
        self._commit()
        self.publish_event()

    def _commit(self):
        self.repo.add(self.storedata)

    def publish_event(self):
        messagebus.handle(events.ProductCreated(id_='1'))

    def rollback(self):
        pass


class UpdateProductUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.repo = ProductRepository()

    def __enter__(self):
        self.id_ = None
        self.storeDataUpdate = None
        return self

    def __exit__(self, *args):
        return super().__exit__(*args)

    def commit(self):
        self._commit()
        self.publish_event()


    def _commit(self):
        self.repo.update(self.id_, self.storeDataUpdate)

    def publish_event(self):
        messagebus.handle(events.ProductUpdated(id_='1', name='dell'))

    def rollback(self):
        self.rollback
