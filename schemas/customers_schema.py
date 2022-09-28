from main import ma 
from marshmallow import fields
from schemas.orders_schema import OrdersSchema

class CustomerSchema(ma.Schema):
    class Meta:
        ordered = True
        #fields do not have to match model fields exactly, they can include or exclude fields. Order is not important here.
        fields = ['customers_id', 'first_name', 'last_name', 'address', 'postcode', 'phone']
    orders = fields.List(fields.Nested(OrdersSchema, only=("shipping_date", "to_address")))
#schema for 1 customer only
customer_schema = CustomerSchema()

#schema for multiple customers
customers_schema = CustomerSchema(many=True)