from main import ma 

class GpuSchema(ma.Schema):
    class Meta:
        fields = ['gpu_type', 'gpu_name', 'voltage_required', 'price', 'rating']
    gpu_type = ma.Integer(required=True)
    gpu_name = ma.String(required=True)
    voltage_required = ma.Integer(required=True)
    price = ma.Integer(required=True)
    rating = ma.Integer(required=True)
gpu_schema = GpuSchema()
gpus_schema = GpuSchema(many=True)