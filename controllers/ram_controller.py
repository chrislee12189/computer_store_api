from flask import Blueprint 
from flask import jsonify
from flask import request
from main import db 
from schemas.ram_schema import ram_schema, single_ram_schema
from models.ram import Ram 
from marshmallow.exceptions import ValidationError
from flask_jwt_extended import get_jwt_identity, jwt_required


ram = Blueprint('ram', __name__, url_prefix='/ram')

#ALL ram on database
@ram.route('/', methods=['GET'])
def all_ram():
    ram_list = Ram.query.all()
    result = ram_schema.dump(ram_list)
    return jsonify(result)

#SINGLE ram on database
@ram.route('/<int:id>', methods=['GET'])
def single_ram(id):
    ram_list = Ram.query.get(id)
    if not ram_list:
        return {"Error": "Invalid ID, could not find RAM, please try again."}, 404
    result = single_ram_schema.dump(ram_list)
    return jsonify(result)

#POST ram to database
@ram.route('/', methods=['POST'])
def create_ram():
    ram_fields = single_ram_schema.load(request.json)
    new_ram = Ram(
        ram_type = ram_fields['ram_type'],
        ram_size = ram_fields['ram_size'],
        ram_name = ram_fields['ram_name'],
        price = ram_fields['price'],
        rating = ram_fields['rating'],
    )
    db.session.add(new_ram)
    db.session.commit()
    return jsonify(single_ram_schema.dump(new_ram))

#DELETE ram from database
@ram.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_ram(id):
    if get_jwt_identity() != 'admin':
        return {"Message":"Administrator access only, if you are an administrator, please log in."}, 403
    ram = Ram.query.get(id)
    if not ram:
        return {"Error":"Invalid ID, please re-enter the ID and try again."}, 404
    db.session.delete(ram)
    db.session.commit()
    return {"Message":"Successfully deleted the ram. This is permenant. To re-add the RAM, POST it to the database."}
    

#UPDATE ram on the database
@ram.route('/<int:id>', methods=['PUT'])
def update_ram(id):
    ram = Ram.query.get(id)
    if not ram:
        return {"Error":"Cannot find that ram on the database. Please re-enter a different ID and try again."}, 404
    ram_fields = single_ram_schema.load(request.json)
    ram.ram_type = ram_fields['ram_type']
    ram.ram_size = ram_fields['ram_size']
    ram.ram_name = ram_fields['ram_name']
    ram.price = ram_fields['price']
    ram.rating = ram_fields['rating']
    db.session.commit()
    return jsonify(single_ram_schema.dump(ram))

@ram.errorhandler(ValidationError)
def register_validation_errors(error):
    return error.messages, 400