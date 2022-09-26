from flask import Blueprint 
from flask import jsonify
from flask import request
from main import db 
from schemas.cpu_schema import cpu_schema, cpus_schema
from models.cpu import Cpu

cpu = Blueprint('cpu', __name__, url_prefix ='/cpu')
#Multiple CPUs
@cpu.route('/', methods = ['GET'])
def all_cpu():
    cpu_list = Cpu.query.all()
    result = cpus_schema.dump(cpu_list)
    return jsonify(result)
#1 CPU
@cpu.route('/<int:id>', methods = ['GET'])
def get_cpu(id):
    cpu = Cpu.query.get(id)
    if not cpu:
        return {"Error": "Sorry, that CPU was not found, try a different ID."}
    result = cpu_schema.dump(cpu)
    return jsonify(result)

#POST method
@cpu.route('/', methods = ['POST'])
def create_cpu():
    cpu_fields = cpu_schema.load(request.json)
    new_cpu = Cpu(
        cpu_type = cpu_fields['cpu_type'],
        cpu_name = cpu_fields['cpu_name'],
        cpu_price = cpu_fields['cpu_price'],
        cpu_rating = cpu_fields['cpu_rating']
    )
    db.session.add(new_cpu)
    db.session.commit()
    return jsonify(cpu_schema.dump(new_cpu))

#DELETE cpu
@cpu.route('/<int:id>', methods = ['DELETE'])
def del_cpu(id):
    cpu = Cpu.query.get(id)
    if not cpu:
        return {"Error": "Sorry, cannot find that CPU, please re enter the ID or try a different one."}
    db.session.delete(cpu)
    db.session.commit()
    return {"Message":"Successfully deleted CPU."}

#UPDATE cpu

@cpu.route('/<int:id>', methods = ['PUT'])
def update_cpu(id):
    cpu = Cpu.query.get(id)
    if not cpu:
        return {"Error":"Sorry, cannot find that CPU, please re enter the ID or try a different one."}
    cpu_fiels = cpu_schema.load(request.json)
    cpu.cpu_type = cpu_fiels['cpu_type']
    cpu.cpu_name = cpu_fiels['cpu_name']
    cpu.cpu_price = cpu_fiels['cpu_price']
    cpu.cpu_rating = cpu_fiels['cpu_rating']
    db.session.commit()
    return jsonify(cpu_schema.dump(cpu))