from typing import List

class ShoppingCart:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def add(self, item):
        if self.size() == self.max_size:
            raise OverflowError("cannot add more items")
        self.items.append(item)

    def size(self):
        return len(self.items)

    def get_items(self):
        return self.items

    def get_total_price(self, price_map):
        pass
