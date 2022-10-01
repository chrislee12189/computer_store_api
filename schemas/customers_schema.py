from main import ma 
from marshmallow import fields
from schemas.orders_schema import OrdersSchema


class CustomerSchema(ma.Schema):
    class Meta:
        ordered = True
        #fields do not have to match model fields exactly, they can include or exclude fields. Order is not important here.
        fields = ['customers_id', 'first_name', 'last_name', 'address', 'postcode', 'phone']
    orders = fields.List(fields.Nested(OrdersSchema, only=("shipping_date", "to_address")))
    first_name = ma.String(required=True)
    last_name = ma.String(required=True)
    address = ma.String(required=True)
    postcode = ma.Integer(required=True)
    phone = ma.Integer(required=True)
#schema for 1 customer only
customer_schema = CustomerSchema()

#schema for multiple customers
customers_schema = CustomerSchema(many=True)