from main import ma 

class RamSchema(ma.Schema):
    class Meta:
        fields = ['ram_id', 'ram_type', 'ram_size', 'ram_name', 'price', 'rating']

single_ram_schema = RamSchema()
ram_schema = RamSchema(many=True)

