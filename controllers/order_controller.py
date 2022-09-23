from flask import Blueprint 
from flask import jsonify
from flask import request
from main import db 
from schemas.orders_schema import order_schema, orders_schema
from models.order import Order 

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
        return {"Error":"Sorry, that order was not found. Try to find a different order."}
    result = order_schema.dump(orders_list)
    return jsonify(result)

#post method
@order.route('/', methods = ['POST'])
def create_order():
    #create new order object
    #get the values from the request and load them with the single schema
    order_fields = order_schema.load(request.json)
    new_order = Order(
        customer_name = order_fields['customers_name'],
        to_address = order_fields['to_address'],
        to_postcode = order_fields['to_postcode'],
        shipping_date = order_fields['shipping_date'],
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify(order_schema.dump(new_order))


#random comment for commit after merge