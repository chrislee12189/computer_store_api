from main import ma 


class PsuSchema(ma.Schema):
    class Meta:
        fields = ['psu_type', 'psu_name', 'voltage', 'rating', 'price']


    psu_type = ma.Integer(required=True)
    psu_name = ma.String(required = True)
    voltage = ma.Integer(required = True)
    rating = ma.Integer(required = True)
    price = ma.Integer(required = True)

psu_schema = PsuSchema()

psus_schema = PsuSchema(many=True)