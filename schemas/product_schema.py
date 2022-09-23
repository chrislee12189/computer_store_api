from main import ma 

class ProductSchema(ma.Schema):
    class Meta:
        fields = ['product_id', 'order_id', 'customer_id', 'description', 'quantity', 'product_type', 'price']

#single product
product_schema = ProductSchema()
#multiple products
products_schema = ProductSchema(many=True)