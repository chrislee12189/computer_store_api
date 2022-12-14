from flask import Blueprint 
from flask import jsonify
from flask import request
from main import db 
from schemas.orders_schema import order_schema, orders_schema
from models.order import Order 
from flask_jwt_extended import jwt_required
from marshmallow.exceptions import ValidationError

#! the order controller is used to control end points for creating, retrieving, updating and deleting orders on the database. orders will be linked to a customer with foreign key, jwt authentication will allow users to manage their own orders and will not be exclusive to administrators.

#! anyone can create or update an order, only an admin can delete one however.

order = Blueprint('orders', __name__, url_prefix ="/orders")
#controller is now connected to main file.
#all orders
@order.route('/', methods = ['GET'])
def get_order():
    order_list = Order.query.all()
    result = orders_schema.dump(order_list)
    return jsonify(result)
    

#single order
@order.route('/<int:id>', methods = ['GET'])
def get_orders(id):
    orders_list = Order.query.get(id)
    #use order_schema to serialize the order so it can be converted/displayed to JSON
    #check if we have the order in the database. 
    if not orders_list:
        return {"Error":"Sorry, that order was not found. Try to find a different order."}, 404
    result = order_schema.dump(orders_list)
    return jsonify(result)

#post method

@order.route('/', methods = ['POST'])
def create_order():
    #create new order object
    #get the values from the request and load them with the single schema
    order_fields = order_schema.load(request.json)
    new_order = Order(
        customer_name = order_fields['customer_name'],
        to_address = order_fields['to_address'],
        to_postcode = order_fields['to_postcode'],
        shipping_date = order_fields['shipping_date'],
        customers_id = order_fields['customers_id']
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify(order_schema.dump(new_order))


#delete an order 
#! only available to admin
@order.route('/<int:id>', methods = ['DELETE'])
@jwt_required()
def delete_order(id):
    order = Order.query.get(id)
    if not order:
        return {"Error": "Cannot delete an order that does not exsist. Please enter an order that exsists."}, 404
    db.session.delete(order)
    db.session.commit()
    return {"Message": "Successfully deleted order."}

#update order
@order.route('/<int:id>', methods = ['PUT'])
def update_order(id):
    #find the order/if it even exists
    order = Order.query.get(id)
    if not order:
        return {"message": "Cannot find the order, please enter an exsisting order."}, 404
    order_fields = order_schema.load(request.json)
    order.customer_name = order_fields['customer_name']
    order.to_address = order_fields['to_address']
    order.to_postcode= order_fields['to_postcode']
    order.shipping_date = order_fields['shipping_date']
    #session already exists so just need to commit changes for this method.
    db.session.commit()
    return jsonify(order_schema.dump(order))

@order.errorhandler(ValidationError)
def register_validation_errors(error):
    return error.messages, 400