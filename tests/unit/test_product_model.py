def test_new_product(new_product):
    """
    GIVEN a Product model
    WHEN a new Product is created
    THEN check the name, description fields are defined correctly
    """
    assert new_product.name == "Test Name"
    assert new_product.description == "Test Description"


def test_product_update(new_product):
    """
    GIVEN a Product model
    WHEN a Product is updated
    THEN check the name, description fields are defined correctly
    """
    new_product.update({"name": "New Test Name", "description": "New Test Description"})
    assert new_product.name == "New Test Name"
    assert new_product.description == "New Test Description"

