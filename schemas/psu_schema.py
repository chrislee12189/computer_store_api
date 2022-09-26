from main import ma 

class PsuSchema(ma.Schema):
    class Meta:
        fields = ['psu_type', 'psu_name', 'voltage', 'rating', 'price']

psu_schema = PsuSchema()

psus_schema = PsuSchema(many=True)