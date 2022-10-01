from main import ma 

class MotherboardSchema(ma.Schema):
    class Meta:
        fields = ['motherboard_id', 'motherboard_type', 'motherboard_name', 'price', 'rating']

    motherboard_type = ma.Integer(required=True)
    motherboard_name = ma.String(required=True)
    price = ma.Integer(required=True)
    rating = ma.Integer(required=True)




#single board
motherboard_schema = MotherboardSchema()
#multiple boards
motherboards_schema = MotherboardSchema(many=True)