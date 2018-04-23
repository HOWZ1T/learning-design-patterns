from Builder.meal import Meal
from Builder import products


class MealBuilder:
    @staticmethod
    def prepare_veggie_burger():
        meal = Meal()
        meal.add_item(products.VeggieBurger())
        meal.add_item(products.Coke())

        return meal

    @staticmethod
    def prepare_normal_meal():
        meal = Meal()
        meal.add_item(products.ChickenBurger())
        meal.add_item(products.Pepsi())

        return meal
