from shopping_cart import ShoppingCart
from item_database import ItemDataBase
from unittest.mock import Mock

import pytest

@pytest.fixture
def cart():
    #All setup for the cart here...
    return ShoppingCart(5)

def test_can_add_item_to_cart(cart):
    cart.add("apple")
    assert cart.size() == 1

def test_when_item_added_then_cart_contains_item(cart):
    cart.add("apple")
    assert "apple" in cart.get_items()

def test_when_add_more_than_max_items_should_fail(cart):
    for _ in range(5):
        cart.add("apple")

    with pytest.raises(OverflowError):
        cart.add("apple")

def test_can_get_total_price(cart):
    cart.add("apple")
    cart.add("orange")

    item_database = ItemDataBase()
    item_database.get = Mock(return_value=1.0)
    assert cart.get_total_price(item_database) == 2
