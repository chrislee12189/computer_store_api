from flask import Blueprint 
from flask import jsonify
from flask import request
from main import db 
from models.customers import Customer 
from schemas.customers_schema import customer_schema, customers_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow.exceptions import ValidationError

#! the customers controller is used to control end points for creating, retrieving, updating and deleting customers

#! anyone can create and update a customer, only admins can delete them however.


#url prefix is an attribute of Blueprint, so use url, not uri here.
#customers temporarily spelled incorrectly so i could check thatmy controller registered correctly. it did. Controller is now connected to main file.
customers = Blueprint('customers', __name__, url_prefix='/customers')

@customers.route('/', methods=['GET'])
def get_customers():
    #access all customers on database
    customers_list = Customer.query.all()
    result = customers_schema.dump(customers_list)
    return jsonify(result), 200




#integer id specifies customer_id
@customers.route('/<int:id>', methods=['GET'])
def get_customer(id):
    #access 1 customer on database by choosing customer_id
    #get query will retrieve primary_key (which is customer_id)
    customer_list = Customer.query.get(id)
    if not customer_list:
        return {"Error": "Customer not found."}, 418
        # yes, i know that the error code shouldve been 404 not found, but who can go past 418 :P
    result = customer_schema.dump(customer_list)
    return jsonify(result), 200




#create new customer
@customers.route('/', methods=['POST'])
def create_customer():
    customer_fields = customer_schema.load(request.json)
    customer = Customer(
        first_name = customer_fields['first_name'], 
        last_name = customer_fields['last_name'],
        address = customer_fields['address'],
        postcode = customer_fields['postcode'],
        phone = customer_fields['phone'],
    )
    db.session.add(customer)
    db.session.commit()
    return jsonify(customer_schema.dump(customer))




#update exsisting customer
@customers.route('/<int:id>', methods=['PUT'])
def update_customer(id):
    customer = Customer.query.get(id)
    if not customer:
        return {"Error: Customer does not exsist, to update a customer, enter an exsisting customer."}
    customer_fields = customer_schema.load(request.json)
    customer.first_name= customer_fields['first_name']
    customer.last_name= customer_fields['last_name']
    customer.address= customer_fields['address']
    customer.postcode= customer_fields['postcode']
    customer.phone= customer_fields['phone']
    db.session.commit()
    return jsonify(customer_schema.dump(customer))




#DELETE customer 
#! only available to admin
@customers.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_customer(id):
    print(get_jwt_identity())
    if get_jwt_identity() != 'admin':
        return {"DENIED": "You do not have permission to delete, only an administrator can delete. If you are an administrator, check your token and try again."}, 403

    customer = Customer.query.get(id)
    if not customer:
        return {"Error":"Could not find that customer, please enter existing customer id in order to delete a customer."}
    db.session.delete(customer)
    db.session.commit()
    return {'Success': 'Customer successfully removed from database. This change is permenant, to re add the customer, POST the details.'}, 200



@customers.errorhandler(ValidationError)
def register_validation_errors(error):
    return error.messages, 400