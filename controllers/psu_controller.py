from flask import Blueprint 
from flask import jsonify
from flask import request
from main import db 
from schemas.psu_schema import psu_schema, psus_schema
from models.psu import Psu
from marshmallow.exceptions import ValidationError
from flask_jwt_extended import get_jwt_identity, jwt_required



psu = Blueprint('psu', __name__, url_prefix='/psu')
#ALL psu
@psu.route('/', methods=['GET'])
def get_psus():
    psu_list = Psu.query.all()
    result = psus_schema.dump(psu_list)
    return jsonify(result)

#1 psu
@psu.route('/<int:id>', methods=['GET'])
def find_psu(id):
    psu = Psu.query.get(id)
    if not psu:
        return {"Error":"Sorry, that PSU was not found. Try to find a different PSU."}, 404
    result = psu_schema.dump(psu)
    return jsonify(result)

#POST psu
@psu.route('/', methods = ['POST'])
def create_psu():
    psu_fields = psu_schema.load(request.json)
    new_psu = Psu(
        psu_type = psu_fields['psu_type'],
        psu_name = psu_fields['psu_name'],
        voltage = psu_fields['voltage'],
        rating = psu_fields['rating'],
        price = psu_fields['price']
    )
    db.session.add(new_psu)
    db.session.commit()
    return jsonify(psu_schema.dump(new_psu))

#DELETE psu
@psu.route('/<int:id>', methods = ['DELETE'])
@jwt_required()
def delete_psu(id):
    if get_jwt_identity() != 'admin':
        return {"Message":"Administrator access only, if you are an administrator, please log in, if you are not an administrator, you cannot access this method."}, 403
    psu = Psu.query.get(id)
    if not psu:
        return {"Error": "Cannot delete an order that does not exsist. Please enter an order that exsists."}, 404
    db.session.delete(psu)
    db.session.commit()
    return {"Message": "Successfully deleted PSU."}, 201

#UPDATE psu
@psu.route('/<int:id>', methods = ['PUT'])
@jwt_required()
def update_psu(id):
    if get_jwt_identity() != 'admin':
        return {"Message":"Administrator access only, if you are an administrator, please log in, if you are not an administrator, you cannot access this method."}, 403
    psu = Psu.query.get(id)
    if not psu:
        return {"Message": "Cannot find the PSU, please enter an exsisting PSU and try again."}, 404
    psu_fields = psu_schema.load(request.json)
    psu.psu_type = psu_fields['psu_type'],
    psu.psu_name = psu_fields['psu_name'],
    psu.voltage = psu_fields['voltage'],
    psu.rating = psu_fields['rating'],
    psu.price = psu_fields['price'],

    db.session.commit()
    return jsonify(psu_schema.dump(psu))


@psu.errorhandler(ValidationError)
def register_validation_errors(error):
    return error.messages, 400