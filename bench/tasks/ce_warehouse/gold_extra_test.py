"""Hidden checks added by Kytest-Agents.

The upstream tests never read inventory after an order. The skeleton's own
example (add 3, order 2) and create_order's "quantity is not adequate" rule
imply that stock is reserved by an order; a second order must see the reduced stock.
"""
from solution import Warehouse


def test_order_reduces_stock():
    w = Warehouse()
    w.add_product(1, "product1", 3)
    w.create_order(1, 1, 2)
    assert w.get_product_quantity(1) == 1
    assert w.create_order(2, 1, 2) is False
