from .OfferSchema import OfferSchema
from marshmallow import Schema, fields


class ProductSchema(Schema):
    class Meta:
        ordered = True

    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    offers = fields.List(fields.Nested(lambda: OfferSchema()))
