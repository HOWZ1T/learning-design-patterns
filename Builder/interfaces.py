import abc


class Item:
    @abc.abstractmethod
    def name(self):
        raise NotImplementedError("users must implement the method name to use this base class")

    @abc.abstractmethod
    def packing(self):
        raise NotImplementedError("users must implement the method packing to use this base class")

    def price(self):
        raise NotImplementedError("users must implement the method price to use this base class")


class Packing:
    @abc.abstractmethod
    def pack(self):
        raise NotImplementedError("users must implement the method pack to use this base class")
