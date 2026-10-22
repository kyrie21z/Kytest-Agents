# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

"""Test P2: Accumulate quantity on an existing product."""
from solution import Warehouse

def test_p2_accumulate_quantity():
    warehouse = Warehouse()
    warehouse.add_product(1, "Widget", 10)
    warehouse.add_product(1, "Widget", 5)
    assert warehouse.inventory[1]["quantity"] == 15
