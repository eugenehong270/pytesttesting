from typing import List

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def get_items(self):
        pass

    def get_total_price(self, price_map):
        pass
