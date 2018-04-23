import abc


class Shape:
    @staticmethod
    @abc.abstractmethod
    def draw():
        raise NotImplementedError("users must implement draw to use this base class")


class Rectangle(Shape):
    @staticmethod
    def draw():
        print("inside rectangle draw method")


class Square(Shape):
    @staticmethod
    def draw():
        print("inside square draw method")


class Circle(Shape):
    @staticmethod
    def draw():
        print("inside circle draw method")
