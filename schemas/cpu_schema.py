from main import ma 
from marshmallow.validate import Length


class CpuSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ['cpu_id','cpu_type', 'cpu_name', 'price', 'rating']
    cpu_type = ma.Integer(validate = Length(min=1, max=2))
    cpu_name = ma.String(required=True)
    price = ma.Integer(validate = Length(min=1, max=2000), required=True)
    rating = ma.Integer(required=True)


#1 CPU
cpu_schema = CpuSchema()
#Mulitple CPUs
cpus_schema = CpuSchema(many=True)