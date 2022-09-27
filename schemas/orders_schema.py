from main import ma 
from marshmallow import fields
# from schemas.customers_schema import CustomerSchema


class OrdersSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ['customer_name', 'to_address', 'to_postcode','shipping_date', 'customers_id', 'customer']
        #! loads but does not display
        load_only = ['customers_id']
customer = fields.Nested('CustomerSchema', only = ('customer_name', 'order_id','postcode'))
#single order
order_schema = OrdersSchema()

#mulitple orders
orders_schema = OrdersSchema(many=True)