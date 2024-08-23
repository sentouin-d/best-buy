import pytest
from products import Product

def test_creating_prod():
    prod = Product("test", 2, 1)
    assert prod.get_quantity() == 1

def test_created_prod_invalid_details():
    with pytest.raises(ValueError):
        prod = Product("", 2, 1)

def test_prod_updated_quantity():
    prod = Product("test", 2, 2)
    purchased = prod.buy(1)
    assert purchased == 2
    assert prod.get_quantity() == 1

def test_prod_becomes_inactive():
    prod = Product("test", 2, 1)
    prod.buy(2)
    assert not prod.is_active()