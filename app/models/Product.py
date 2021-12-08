from app import db
from .Offer import Offer


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    offers = db.relationship('Offer', cascade="all,delete", backref='product')

    def __init__(self, product):
        self.name = product.get('name')
        self.description = product.get('description')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_single_product(id):
        return Product.query.get(id)

    @staticmethod
    def get_all_products():
        return Product.query.all()
