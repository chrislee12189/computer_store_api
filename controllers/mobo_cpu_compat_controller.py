from flask import Blueprint 
from flask import jsonify

from models.mobo_cpu_compat import Compat
from schemas.mobo_cpu_compat_schema import multi_compat


compatibility = Blueprint('compatibility', __name__, url_prefix='/compatibility')


#! THIS CONTROLLER RETURNS A LIST OF ALL CPUS AND MOTHERBOARDS THAT ARE COMPATIBLE WITH EACH OTHER
#GET compatibilte mobo and cpu
@compatibility.route('/', methods=['GET'])
def get_compat():
    compat_list = Compat.query.all()
    result = multi_compat.dump(compat_list)
    return jsonify(result)

