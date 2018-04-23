from Abstract_Factory import interfaces


# SHAPES
class Circle(interfaces.Shape):
    def draw(self):
        print("O -- inside circle draw method")


class Square(interfaces.Shape):
    def draw(self):
        print("[] -- inside square draw method")


class Rectangle(interfaces.Shape):
    def draw(self):
        print("[   ] -- inside rectangle draw method")


# COLORS
class Red(interfaces.Color):
    def fill(self):
        print("inside red fill method")


class Green(interfaces.Color):
    def fill(self):
        print("inside green fill method")


class Blue(interfaces.Color):
    def fill(self):
        print("inside blue fill method")
