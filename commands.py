from flask import Blueprint
from main import db 
from models.customers import Customer 
from models.order import Order 
from models.product import Product
from models.motherboards import Motherboards
from models.cpu import Cpu
from models.gpu import Gpu
from models.psu import Psu
from models.ram import Ram
from models.ratings import Ratings
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
#CREATE ORIGINAL ENTRY FOR ALL TABLES. REMAINDER OF THE DATA WILL BE ADDED VIA POST METHOD.
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

    product1 = Product(
        description = 'ASUS Prime A520M-K. (Type 1)',
        quantity = 1,
        product_type = 'AMD Socket',
        price = 299
    )
    db.session.add(product1)
    motherboard1 =Motherboards(
        motherboard_type = 1,
        motherboard_name = 'Aorus x570s elite (AMD Socket)',
        price = 350,
        rating = 5
        
    )
    db.session.add(motherboard1)
    cpu1 = Cpu(
        cpu_type = 1,
        cpu_name = 'Ryzen 7 3700x (AM4)',
        price = 360,
        rating = 3
    )
    db.session.add(cpu1)
    gpu1 = Gpu(
        gpu_type = 1,
        gpu_name = 'Aorus Master RTX 3070 LHR 8GB',
        voltage_required = 650,
        rating = 5
    )
    db.session.add(gpu1)

    psu1 = Psu(
        psu_type = 1,
        psu_name = 'Thermaltake ToughPower Gold 750W',
        voltage = 750,
        rating = 4
    )
    db.session.add(psu1)

    ram1 = Ram(
        ram_type = "DDR4",
        ram_size = 16,
        ram_name = "Team T Force Delta 16GB 3200MHz CL16",
        price = 99,
        rating = 4
    )
    db.session.add(ram1)
    
    rating1 = Ratings(
        test = "Testing. Ratings will use foreign keys to collect info."
    )
    db.session.add(rating1)






    db.session.commit()
    print('Table seeded')