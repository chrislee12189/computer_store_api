from main import ma 

class GpuSchema(ma.Schema):
    class Meta:
        fields = ['gpu_type', 'gpu_name', 'voltage_required', 'price', 'rating']
gpu_schema = GpuSchema()
gpus_schema = GpuSchema(many=True)