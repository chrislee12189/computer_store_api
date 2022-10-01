from flask import Blueprint 
from flask import jsonify
from flask import request
from main import db 
from models.motherboards import Motherboards
from schemas.motherboard_schema import motherboard_schema, motherboards_schema
from marshmallow.exceptions import ValidationError

motherboards = Blueprint('motherboards', __name__, url_prefix='/motherboards')

#get all motherboards in database
@motherboards.route('/', methods=['GET'])
def all_motherboards():
    motherboards = Motherboards.query.all()
    if not motherboards:
        return {"Error": "No motherboard found, please check your entry and try again."}, 404
    result = motherboards_schema.dump(motherboards)
    return jsonify(result)

#get 1 motherboard in database
@motherboards.route('/<int:id>', methods=['GET'])
def get_motherboard(id):
    motherboard = Motherboards.query.get(id)
    if not motherboard:
        return {"Error": "No motherboard found, please check your entry and try again."}, 404
    result = motherboard_schema.dump(motherboard)
    return jsonify(result)

#CREATE motherboard
@motherboards.route('/', methods=['POST'])
def create_motherboard():
    mobo_fields = motherboard_schema.load(request.json)
    new_mobo = Motherboards(
        motherboard_type = mobo_fields['motherboard_type'],
        motherboard_name = mobo_fields['motherboard_name'],
        price = mobo_fields['price'],
        rating = mobo_fields['rating'],
    )
    db.session.add(new_mobo)
    db.session.commit()
    return jsonify(motherboard_schema.dump(new_mobo))

#UPDATE exsisting motherboard
@motherboards.route('/<int:id>', methods = ['PUT'])
def update_motherboard(id):
    motherboard = Motherboards.query.get(id)
    if not motherboard:
        return {"Error": "No motherboard found, please check your entry and try again."}, 404
    motherboard_fields = motherboard_schema.load(request.json)
    motherboard.motherboard_type = motherboard_fields['motherboard_type']
    motherboard.motherboard_name = motherboard_fields['motherboard_name']
    motherboard.price = motherboard_fields['price']
    motherboard.rating = motherboard_fields['rating']
    db.session.commit()
    return jsonify(motherboard_schema.dump(motherboard))

@motherboards.route('/<int:id>', methods = ['DELETE'])
def delete_motherboard(id):
    motherboard = Motherboards.query.get(id)
    if not motherboard:
        return {"Error": "No motherboard found, please check your entry and try again."},404
    db.session.delete(motherboard)
    db.session.commit()
    return {'Success':'You have successfully deleted the motherboard from our database. This change is permenant, the Motherboards can be re-added to the database using the POST method.'},202

@motherboards.errorhandler(ValidationError)
def register_validation_errors(error):
    return error.messages, 400