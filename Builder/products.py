from Builder import abstract_objects


class VeggieBurger(abstract_objects.Burger):
    def price(self):
        return float(25.0)

    def name(self):
        return "Veggie Burger"


class ChickenBurger(abstract_objects.Burger):
    def price(self):
        return float(50.5)

    def name(self):
        return "Chicken Burger"


class Coke(abstract_objects.ColdDrink):
    def price(self):
        return float(30.0)

    def name(self):
        return "Coke"


class Pepsi(abstract_objects.ColdDrink):
    def price(self):
        return float(35.0)

    def name(self):
        return "Pepsi"
