from flask import Blueprint 
from flask import jsonify
# from flask import request
# from main import db 
from schemas.orders_schema import order_schema, orders_schema
# from schemas.customers_schema import customer_schema
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
    result = order_schema.dump(orders_list)
    return jsonify(result)
