from flask import Blueprint
from flask import jsonify
from models.voltage_req import VoltageReq
from schemas.voltage_req_schema import voltages_schema,voltage_schema
from marshmallow.exceptions import ValidationError


voltages = Blueprint('voltages', __name__, url_prefix='/voltages')


#GET voltages, this is inteded to be GET only. In future, POSTING a voltage is intended to be only accessible to customers who have an order ID or maybe admins as well at some point. I dont have time for that at the moment, so it will be added as a feature for future versions.


@voltages.route('/', methods=['GET'])
def get_voltage():
    voltage_list = VoltageReq.query.all()
    result = voltages_schema.dump(voltage_list)
    return jsonify(result)

@voltages.route('/<int:id>', methods=['GET'])
def check_voltage(id):
    voltage = VoltageReq.query.get(id)
    if not voltage:
        return {"Error": "No such voltage compatiblility comparison has been found with the ID you provided. Please try a different comparison ID."}, 404
    result = voltage_schema.dump(voltage)
    return jsonify(result)


@voltages.errorhandler(ValidationError)
def register_validation_errors(error):
    return error.messages, 400