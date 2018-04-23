class Meal:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def get_cost(self):
        cost = float(0)

        for item in self._items:
            cost += item.price()

        return cost

    def show_items(self):
        for item in self._items:
            print("Item: {}, Packing: {}, Price: {}".format(item.name(), item.packing().pack(), item.price()))
