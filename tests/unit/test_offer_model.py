
def test_new_offer(new_offer, new_product):
    """
    GIVEN a Offer model
    WHEN a new Offer is created
    THEN check the price, items_in_stock and product_id fields are defined correctly
    """
    assert new_offer.price == 1
    assert new_offer.items_in_stock == 1
    assert new_offer.product_id == new_product.id