# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

from solution import Warehouse

def test_add_product_adds_quantity_on_existing():
    """
    Contract quote: 'Add product to inventory and plus the quantity if it has existed in inventory.'
    Input domain: product_id=1 already exists with quantity 5; add_product(1, 'widget', 3) called again.
    Oracle: Per spec, existing quantity should be incremented by new quantity: 5 + 3 = 8.
    Fault hypothesis: Implementation replaces quantity instead of adding (line 31 uses assignment), so result would be 3 instead of 8.
    """
    wh = Warehouse()
    wh.add_product(1, 'widget', 5)
    wh.add_product(1, 'widget', 3)
    assert wh.inventory[1]['quantity'] == 8
