from flask import Blueprint 
from flask import jsonify
from flask import request
from main import db 
from models.motherboards import Motherboards
from schemas.motherboard_schema import motherboard_schema, motherboards_schema

motherboards = Blueprint('motherboards', __name__, url_prefix='/motherboards')

#get all motherboards in database
@motherboards.route('/', methods=['GET'])
def all_motherboards():
    motherboards = Motherboards.query.all()
    if not motherboards:
        return {"Error": "No motherboard found, please check your entry and try again."}
    result = motherboard_schema.dump(motherboards)
    return jsonify(result)

#get 1 motherboard in database
@motherboards.route('/<int:id>', methods=['GET'])
def get_motherboard(id):
    motherboard = Motherboards.query.get(id)
    if not motherboard:
        return {"Error": "No motherboard found, please check your entry and try again."}
    result = motherboards_schema.dump(motherboard)
    return jsonify(result)

#CREATE motherboard
# @motherboards.route('/create', methods=['POST'])