from marshmallow import Schema, fields


class OfferSchema(Schema):
    class Meta:
        ordered = True

    id = fields.Int()
    price = fields.Int()
    items_in_stock = fields.Int()
    product_id = fields.Int()
