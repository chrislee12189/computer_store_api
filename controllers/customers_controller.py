from flask import Blueprint 
from main import db 
from models.customers import Customer 

#url prefix is an attribute of Blueprint, so use url, not uri here.
customers = Blueprint('customers', __name__, url_prefix='/customers')

@customers.route('/', methods=['GET'])
def get_customers():
    #access all customers on database
    customers_list = customers.query.all()
    