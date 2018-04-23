import abc


class AbstractFactory:
    @abc.abstractmethod
    def get_color(self):
        raise NotImplementedError("users must implement the method get_color to use this base-class!")

    @abc.abstractmethod
    def get_shape(self):
        raise NotImplementedError("users must implement the method get_shape to use this base-class!")
