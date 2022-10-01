from main import ma 

class RamSchema(ma.Schema):
    class Meta:
        fields = ['ram_id', 'ram_type', 'ram_size', 'ram_name', 'price', 'rating']

    ram_type = ma.String(required=True)
    ram_size = ma.Integer(required=True)
    ram_name = ma.String(required=True)
    price = ma.Integer(required=True)
    rating = ma.Integer(required=True)
single_ram_schema = RamSchema()
ram_schema = RamSchema(many=True)

