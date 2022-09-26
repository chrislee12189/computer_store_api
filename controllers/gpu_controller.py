from flask import Blueprint 
from flask import jsonify
from flask import request
from main import db 
from schemas.gpu_schema import gpu_schema, gpus_schema
from models.gpu import Gpu

gpu = Blueprint('gpu', __name__, url_prefix='/gpu')

#ALL gpus
@gpu.route('/', methods=['GET'])
def all_gpu():
    gpu_list = Gpu.query.all()
    result = gpus_schema.dump(gpu_list)
    return jsonify(result)

#SINGLE gpu
@gpu.route('/<int:id>', methods=['GET'])
def get_gpu(id):
    gpu_list = Gpu.query.get(id)
    if not gpu_list:
        return {"Error":"Sorry, that GPU was not found. Try to find a different GPU."}
    result = gpu_schema.dump(gpu_list)
    return jsonify(result) 

#POST method

@gpu.route('/', methods=['POST'])
def create_gpu():
    gpu_fields = gpu_schema.load(request.json)
    new_gpu = Gpu(
        gpu_type = gpu_fields['gpu_type'],
        gpu_name = gpu_fields['gpu_name'],
        voltage_required = gpu_fields['voltage_required'],
        rating = gpu_fields['rating'],
    )
    db.session.add(new_gpu)
    db.session.commit()
    return jsonify(gpu_schema.dump(new_gpu))

#DELETE a GPU
@gpu.route('/', methods=['DELETE'])
def del_gpu(id):
    gpu = Gpu.query.get(id)
    if not gpu:
        return {"Error": "Cannot find that GPU. Please retry with a different ID."}
    db.session.delete(gpu)
    db.session.commit()
    return {"Message": "Successfully deleted GPU."}

#UPDATE GPU
@gpu.route('/<int:id>', methods=['PUT'])
def update_gpu(id):
    gpu = Gpu.query.get(id)
    if not gpu:
        return {"Message": "Unable to locate the GPU. Please re-enter or change the ID and try again."}
    gpu_field = gpu_schema.load(request.json)
    gpu.gpu_type = gpu_field['gpu_type'],
    gpu.gpu_name = gpu_field['gpu_name'],
    gpu.voltage_required = gpu_field['voltage_required'],
    gpu.rating = gpu_field['rating'],