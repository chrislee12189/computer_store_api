from flask import Blueprint 
from flask import jsonify
from main import db 
from models.customers import Customer 
from schemas.customers_schema import customer_schema, customers_schema
#url prefix is an attribute of Blueprint, so use url, not uri here.
#customers temporarily spelled incorrectly so i could check thatmy controller registered correctly. it did. Controller is now connected to main file.
customers = Blueprint('customers', __name__, url_prefix='/customers')

@customers.route('/', methods=['GET'])
def get_customers():
    #access all customers on database
    customers_list = Customer.query.all()
    result = customers_schema.dump(customers_list)
    return jsonify(result)

#integer id specifies customer_id
@customers.route('/<int:id>', methods=['GET'])
def get_customer(id):
    #access 1 customer on database by choosing customer_id
    #get query will retrieve primary_key (which is customer_id)
    #id could be changed to specific customer id that i want to retrieve, say cutomer_id 1, i could enter '1' instead of id and it will work the same.
    customer_list = Customer.query.get(id)
    result = customer_schema.dump(customer_list)
    return jsonify(result)