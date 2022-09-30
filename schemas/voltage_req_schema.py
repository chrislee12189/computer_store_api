from main import ma 

class VoltageSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ['voltage_id', 'product_id', 'gpu_id', 'psu_id', 'gpu_name', 'psu_name', 'voltage_req', 'voltage_supplied', 'comment']

voltage_schema = VoltageSchema()
voltages_schema = VoltageSchema(many = True)