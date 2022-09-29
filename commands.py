from flask import Blueprint
from main import db 
#import the instance, not the class.
from main import bcrypt
from models.admin import Administrator
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
#! flask db drop, flask db create, flask db seed commands 
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

    admin1 = Administrator(
        username = 'Chris',
        email = 'chris@admin.com',
        #encrypt password
        password = bcrypt.generate_password_hash('Weeeeeeeee').decode('utf-8')
    )
    db.session.add(admin1)


    customer1 = Customer(
        first_name = 'John',
        last_name = 'Doe',
        address = '123 Main Street',
        postcode = '1236',
        phone = '0234567891',
        
    )
    db.session.add(customer1)
    #! we need customer_id for the orders foreign key.
    #! we dont get IDs until we commit to the database.
    db.session.commit()
    
    customer2 = Customer(
    first_name = 'Jensen',
    last_name = 'Edric',
    address = '12 Black Dog Drive',
    postcode = '3456',
    phone = '0222568484'
    )
    db.session.add(customer2)

    customer3 = Customer(
        first_name = 'Cornelius',
        last_name = 'Ansel',
        address = '1 Channing Road',
        postcode = '3000',
        phone = '0493827166'
    )
    db.session.add(customer3)
    #!ORDERS WILL NEED MORE INFORMATION. NEED TO ADD WHAT PRODUCTS ARE ORDERED.
    order1 = Order(
        customers_id = customer1.customers_id,
        customer_name = customer1.first_name + " " + customer1.last_name,
        to_address = customer1.address,
        to_postcode = customer1.postcode,

        shipping_date = '2022',
    )
    db.session.add(order1)

    order2 = Order(
        customers_id = customer2.customers_id,
        customer_name = customer2.first_name + " " + customer2.last_name,
        to_address = customer2.address,
        to_postcode = customer2.postcode,
        shipping_date = '2022',
        
    )
    db.session.add(order2)
#!order 3 and 4 belong to customer 3
    order3 = Order(
        customers_id = customer3.customers_id,
        customer_name = customer3.first_name + " " + customer3.last_name,
        to_address = customer3.address,
        to_postcode = customer3.postcode,
        shipping_date = '2022',
        
    )
    db.session.add(order3)

    order4 = Order(
        customers_id = customer3.customers_id,
        customer_name = customer3.first_name + " " + customer3.last_name,
        to_address = customer3.address,
        to_postcode = customer3.postcode,
        shipping_date = '2022',
        
    )
    db.session.add(order4)


    
    #! needs work for foreign key ID
    motherboard1 =Motherboards(
        motherboard_type = 1,
        motherboard_name = 'Aorus x570s elite (AMD Socket)',
        price = 350,
        rating = 5
    )
    db.session.add(motherboard1)
    #! needs work for foreig key ID
    cpu1 = Cpu(
        cpu_type = 1,
        cpu_name = 'ASUS Prime A520M-K. (Type 1)',
        price = 360,
        rating = 3
    )
    db.session.add(cpu1)

    cpu2 = Cpu(
        cpu_type = 1,
        cpu_name = 'Ryzen 9 5900x (Type 1)' ,
        price = 500,
        rating = 5
    )
    db.session.add(cpu2)
    db.session.commit()
    product1 = Product(
        product_id = 1,
        description = cpu1.cpu_name ,
        quantity = 1,
        product_type = 'AMD Socket',
        price = 299,
        cpu_id = cpu1.cpu_id
    )
    db.session.add(product1)

    product2 = Product(
        product_id = 2,
        description = cpu2.cpu_name,
        quantity = 13,
        product_type = 'AMD Socket',
        price = 500,
        cpu_id = cpu2.cpu_id
    )
    db.session.add(product2)
    db.session.commit()


    gpu1 = Gpu(
        gpu_type = 1,
        gpu_name = 'Aorus Master RTX 3070 LHR 8GB',
        voltage_required = 650,
        price = 1050,
        rating = 5,
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