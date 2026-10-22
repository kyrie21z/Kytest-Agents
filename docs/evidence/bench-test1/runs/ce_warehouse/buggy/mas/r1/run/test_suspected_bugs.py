# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

def test_p2_accumulate_existing():
    """Accumulate quantity for an existing product.

    Docstring quote: 'Add product to inventory and plus the quantity if it has existed in inventory.'

    Input domain: product_id=1 already in inventory with quantity 10, then add_product(1, 'Widget', 5).

    Expected result: warehouse.inventory[1]['quantity'] == 15

    Rationale: Specification states: 'plus the quantity if it has existed in inventory.'

    Faulty behavior detected: If the method replaces the quantity instead of accumulating (i.e., quantity becomes 5 instead of 15).
    """
    from solution import Warehouse
    warehouse = Warehouse()
    warehouse.add_product(1, 'Widget', 10)
    warehouse.add_product(1, 'Widget', 5)
    assert warehouse.inventory[1]['quantity'] == 15
