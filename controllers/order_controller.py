from flask import Blueprint 
from main import db 
from models.order import Order 

order = Blueprint('orders', __name__, url_prefix ="/orders")

@order.route('/', methods = ['GET'])
def get_orders():
    order_list = order.query.all()