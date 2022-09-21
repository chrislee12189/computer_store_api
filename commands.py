from flask import Blueprint
from main import db 
from models.customers import Customer 
from models.order import Order 
# from datetime import date 
db_commands = Blueprint('db', __name__)

#create models
@db_commands.cli.command('create')
def create_db():
    # Tell SQLAlchemy to create all tables for all models in the physical database
    db.create_all()
    print('Tables created.')

@db_commands.cli.command('drop')
def drop_db():
    #drop tables
    db.drop_all()
    print('Tables have been dropped successfully.')

@db_commands.cli.command('seed')
def seed_db():
    customer1 = Customer(
        first_name = 'John',
        last_name = 'Doe',
        address = '123 Main Street',
        postcode = '1236',
        phone = '0234567891'
    )
    db.session.add(customer1)
    
    order1 = Order(
        customer_name = 'Jane Doe',
        to_address = '234 West Street',
        to_postcode = '9876',
        shipping_date = '2022'
    )
    db.session.add(order1)
    db.session.commit()
    print('Table seeded')