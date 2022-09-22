from main import ma 


class OrdersSchema(ma.Schema):
    class Meta:
        fields = ['customers_name', 'to_address', 'to_postcode','shipping_date']

#single order
order_schema = OrdersSchema()

#mulitple orders
orders_schema = OrdersSchema(many=True)