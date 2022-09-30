from flask import Blueprint
from flask import jsonify
from models.voltage_req import VoltageReq
from schemas.voltage_req_schema import voltages_schema



voltages = Blueprint('voltages', __name__, url_prefix='/voltages')

#GET voltages

@voltages.route('/', methods=['GET'])
def get_voltage():
    voltage_list = VoltageReq.query.all()
    result = voltages_schema.dump(voltage_list)
    return jsonify(result)