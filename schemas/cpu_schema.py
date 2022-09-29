from main import ma 


class CpuSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ['cpu_type', 'cpu_name', 'price', 'rating']


#1 CPU
cpu_schema = CpuSchema()
#Mulitple CPUs
cpus_schema = CpuSchema(many=True)