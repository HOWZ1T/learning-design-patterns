from Builder.builder import MealBuilder


meal_builder = MealBuilder()
veggie_meal = meal_builder.prepare_veggie_burger()
print("Veggie Burger")
veggie_meal.show_items()
print("Total Cost: {}".format(veggie_meal.get_cost()))

normal_meal = meal_builder.prepare_normal_meal()
print("\n\nNormal Meal")
normal_meal.show_items()
print("Total Cost: {}".format(normal_meal.get_cost()))
