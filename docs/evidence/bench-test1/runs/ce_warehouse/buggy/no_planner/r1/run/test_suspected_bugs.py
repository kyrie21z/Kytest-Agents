# Tests the Reviewer judged correct against the specification; they FAIL on the implementation.

def test_add_product_accumulates_quantity_on_existing():
    """Test that add_product accumulates quantity for existing products per spec."""
    from solution import Warehouse
    w = Warehouse()
    w.add_product(1, 'widget', 3)
    w.add_product(1, 'widget', 2)
    assert w.inventory[1]['quantity'] == 5
