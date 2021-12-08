from app import db


class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    items_in_stock = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __init__(self, data):
        self.id = data.get('id')
        self.price = data.get('price')
        self.items_in_stock = data.get('items_in_stock')
        self.product_id = data.get('product_id')

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
    def get_single_offer(id):
        return Offer.query.get(id)