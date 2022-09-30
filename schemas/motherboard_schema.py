from main import ma 

class MotherboardSchema(ma.Schema):
    class Meta:
        fields = ['motherboard_id', 'motherboard_type', 'motherboard_name', 'price', 'rating']
#single board
motherboard_schema = MotherboardSchema()
#multiple boards
motherboards_schema = MotherboardSchema(many=True)