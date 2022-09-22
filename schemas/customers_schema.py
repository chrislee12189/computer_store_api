from main import ma 


class CustomerSchema(ma.Schema):
    class Meta:
        # ordered = True
        #fields do not have to match model fields exactly, they can include or exclude fields. Order is not important here.
        fields = ['customers_id', 'first_name', 'last_name', 'address', 'postcode', 'phone']

#schema for 1 customer only
customer_schema = CustomerSchema()

#schema for multiple customers
customers_schema = CustomerSchema(many=True)