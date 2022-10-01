from main import ma 
from marshmallow import fields
from schemas.cpu_schema import CpuSchema
from schemas.gpu_schema import GpuSchema
from schemas.psu_schema import PsuSchema
from schemas.ram_schema import RamSchema
from schemas.motherboard_schema import MotherboardSchema


class ProductSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ['product_id', 'order_id', 'customer_id', 'description', 'quantity', 'product_type', 'price', 'cpu_id', 'cpu', 'gpu_id', 'gpu', 'psu_id', 'psu', 'ram_id', 'ram', 'motherboard_id', 'motherboards']
        load_only = ['cpu_id', 'gpu_id', 'psu_id', 'ram_id']
    cpu = fields.Nested(CpuSchema, only =('price','cpu_name'))
    gpu = fields.Nested(GpuSchema, only =('voltage_required','gpu_name'))
    psu = fields.Nested(PsuSchema, only =('voltage', 'psu_name'))
    ram = fields.Nested(RamSchema, only =('ram_size', 'ram_name', 'ram_type'))
    motherboards = fields.Nested(MotherboardSchema, only =('motherboard_type','motherboard_name'))


    description = ma.String(required = True)
    quantity = ma.Integer(required = True)
    product_type = ma.String(required = True)
    price = ma.Integer(required = True)
    product_id =ma.Integer(required = True)
#single product
product_schema = ProductSchema()
#multiple products
products_schema = ProductSchema(many=True)