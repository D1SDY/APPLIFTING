import pytest
from app.models.Product import Product
from app.models.Offer import Offer
from app import create_app, db


@pytest.fixture(scope='module')
def new_product():
    product = Product({"name": "Test Name", "description": "Test Description"})
    return product


@pytest.fixture(scope='module')
def new_offer(new_product):
    offer = Offer({"price": 1, "items_in_stock": 1})
    offer.product_id = new_product.id
    return offer


@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()