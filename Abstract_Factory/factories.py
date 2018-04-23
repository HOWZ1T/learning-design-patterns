from Abstract_Factory.abstract_factory import AbstractFactory
from Abstract_Factory import products


class ShapeFactory(AbstractFactory):
    def get_shape(self, shape_name):
        if shape_name is None:
            return None

        shape_name = shape_name.lower()
        if shape_name == "circle":
            return products.Circle()
        elif shape_name == "rectangle":
            return products.Rectangle()
        elif shape_name == "square":
            return products.Square()

        return None

    def get_color(self, color_name):
        return None


class ColorFactory(AbstractFactory):
    def get_shape(self, shape_name):
        return None

    def get_color(self, color_name):
        if color_name is None:
            return None

        color_name = color_name.lower()
        if color_name == "red":
            return products.Red()
        elif color_name == "green":
            return products.Green()
        elif color_name == "blue":
            return products.Blue()

        return None


class FactoryProducer:
    @staticmethod
    def get_factory(choice):
        if choice is None:
            return None

        choice = choice.lower()

        if choice == "shape":
            return ShapeFactory()
        elif choice == "color":
            return ColorFactory()

        return None
