from Builder import packing_objects
from Builder import interfaces
import abc


class Burger(interfaces.Item):
    def packing(self):
        return packing_objects.Wrapper()

    @abc.abstractmethod
    def price(self):
        raise NotImplementedError("users must implement the method price to use this base class")


class ColdDrink(interfaces.Item):
    def packing(self):
        return packing_objects.Bottle()

    @abc.abstractmethod
    def price(self):
        raise NotImplementedError("users must implement the method price to use this base class")
