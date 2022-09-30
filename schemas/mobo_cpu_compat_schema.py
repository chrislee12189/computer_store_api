from main import ma
from marshmallow import fields
from schemas.cpu_schema import CpuSchema
from schemas.motherboard_schema import MotherboardSchema


class CompatSchema(ma.Schema):
    class Meta:
        ordered = True
        fields =['compat_id','compatible','cpu_rating', 'motherboard_rating','motherboard', 'cpu']
    cpu = fields.Nested(CpuSchema, ordered =True, only =('cpu_id', 'cpu_name', 'cpu_type'))
    motherboard = fields.Nested(MotherboardSchema,ordered =True, only =('motherboard_id', 'motherboard_name','motherboard_type'))


compat_schema = CompatSchema()
multi_compat = CompatSchema(many=True)