from marshmallow import Schema, fields

class HotelSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    location = fields.Str(required=True)
    rating = fields.Float(required=True)

hotel_schema = HotelSchema()