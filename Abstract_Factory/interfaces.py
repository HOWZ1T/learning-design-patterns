import abc


class Shape:
    @abc.abstractmethod
    def draw(self):
        raise NotImplementedError("users must implement the method draw to use this base-class!")


class Color:
    @abc.abstractmethod
    def fill(self):
        raise NotImplementedError("users must implement the method fill to use this base-class!")
