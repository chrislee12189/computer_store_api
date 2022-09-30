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
from models.mobo_cpu_compat import Compat 


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
#! CREATE INSTANCE IN OWN ITEMS TABLE FIRST BEFORE REFERENCING IN PRODUCT TABLE

#!-----------------------------------------MOTHERBOARDS---------------------------------------------------------!#
    motherboard1 =Motherboards(
        motherboard_type = 1,
        motherboard_name = 'Aorus x570s elite (AM4 Socket)',
        price = 350,
        rating = 5
    )
    db.session.add(motherboard1)


    motherboard2 = Motherboards(
        motherboard_type = 1,
        motherboard_name = "ASUS ROG Crosshair VIII Impact (AM4 Socket)",
        price = 479,
        rating = 5
    )
    db.session.add(motherboard2)


    motherboard3 = Motherboards(
        motherboard_type = 2,
        motherboard_name = "ASUS Prime B560M-A (LGA1200 Socket)",
        price = 159,
        rating = 3
    )
    db.session.add(motherboard3)


    motherboard4 = Motherboards(
        motherboard_type = 2,
        motherboard_name = "MSI MPG Z590 Gaming Plus (LGA1200 Socket)",
        price = 159,
        rating = 5
    )
    db.session.add(motherboard4)
    db.session.commit()


#!-----------------------------------------CPU---------------------------------------------------------!#
    cpu1 = Cpu(
        cpu_type = 1,
        cpu_name = 'ASUS Prime A520M-K. (AMD)',
        price = 360,
        rating = 3
    )
    db.session.add(cpu1)



    cpu2 = Cpu(
        cpu_type = 1,
        cpu_name = 'Ryzen 9 5900x (AMD)' ,
        price = 500,
        rating = 5
    )
    db.session.add(cpu2)
    
    cpu3 = Cpu(
        cpu_type = 2,
        cpu_name = "Intel Core i7 12700KF",
        price = 599,
        rating = 5
    )
    db.session.add(cpu3)


    cpu4 = Cpu(
        cpu_type = 2,
        cpu_name = "Intel Core i9 12900FK",
        price = 899,
        rating = 5
    )
    db.session.add(cpu4)
    db.session.commit()
#!-----------------------------------------GPU--------------------------------------------------------!#
    gpu1 = Gpu(
        gpu_type = 1,
        gpu_name = 'Aorus Master RTX 3070 LHR 8GB',
        voltage_required = 650,
        price = 1050,
        rating = 5,
    )
    db.session.add(gpu1)

    gpu2 = Gpu(
        gpu_type = 1,
        gpu_name = 'Gigabyte RTX 3060 TI LHR 8GB',
        voltage_required = 650,
        price = 699,
        rating = 3
    )
    db.session.add(gpu2)
    db.session.commit()
#!-------------------------------------------PSU---------------------------------------------------------!#
    psu1 = Psu(
        psu_type = 1,
        psu_name = 'Thermaltake ToughPower Gold 750W',
        voltage = 750,
        price = 139,
        rating = 4
    )
    db.session.add(psu1)

    psu2 = Psu(
        psu_type = 2,
        psu_name = 'Segotep ATX  Gold 700W',
        voltage = 700,
        price = 107,
        rating = 3
    )
    db.session.add(psu2)
    db.session.commit()

#!-----------------------------------------RAM---------------------------------------------------------!#
    ram1 = Ram(
        ram_type = "DDR4",
        ram_size = 16,
        ram_name = "Team T Force Delta 16GB 3200MHz CL16",
        price = 99,
        rating = 4
    )
    db.session.add(ram1)
    

    ram2 = Ram(
        ram_type = "DDR4",
        ram_size = 16,
        ram_name = "Corsair Dominator 16GB 3200MHz CL16",
        price = 165,
        rating = 5
    )
    db.session.add(ram2)

    ram3 = Ram(
        ram_type = "DDR5",
        ram_size = 32,
        ram_name = "Corsair Vengeance 32GB 5600MHz CL36",
        price = 319,
        rating =5
    )
    db.session.add(ram3)
    db.session.commit()

#! PRODUCTS LAST SO THAT THEY CAN REFERENCE SPECIFIC IDS FROM OTHER TABLES
    product1 = Product(
        product_id = 1,
        description = cpu1.cpu_name ,
        quantity = 1,
        product_type = 'AMD Socket',
        price = cpu1.price,
        cpu_id = cpu1.cpu_id
    )
    db.session.add(product1)

    product2 = Product(
        product_id = 2,
        description = cpu2.cpu_name,
        quantity = 13,
        product_type = 'AMD Socket',
        price = cpu2.price,
        cpu_id = cpu2.cpu_id
    )
    db.session.add(product2)
    db.session.commit()

    product3 =Product(
        product_id = 3,
        description = gpu1.gpu_name,
        quantity = 30,
        product_type = "LHR",
        price = gpu1.price,
        gpu_id = gpu1.gpu_id
    )
    db.session.add(product3)

    product4 = Product(
        product_id = 4,
        description = gpu2.gpu_name,
        quantity = 11,
        product_type = "LHR",
        price = gpu2.price,
        gpu_id = gpu2.gpu_id
    )
    db.session.add(product4)
    db.session.commit()

    product5 = Product(
        product_id = 5,
        description = psu1.psu_name,
        quantity = 15,
        product_type = "Modular",
        price = psu1.price,
        psu_id = psu1.psu_id
    )
    db.session.add(product5)

    product6 = Product(
        product_id = 6,
        description = psu2.psu_name,
        quantity = 25,
        product_type = "NON-Modular",
        price = psu2.price,
        psu_id = psu2.psu_id
    )
    db.session.add(product6)
    db.session.commit()


    product7 = Product(
        product_id = 7,
        description = ram1.ram_name,
        quantity = 30,
        product_type = ram1.ram_type,
        price = ram1.price,
        ram_id = ram1.ram_id
    )
    db.session.add(product7)

    product8 = Product(
        product_id = 8,
        description = ram2.ram_name,
        quantity = 30,
        product_type = ram2.ram_type,
        price = ram2.price,
        ram_id = ram2.ram_id
    )
    db.session.add(product8)

    product9 = Product(
        product_id = 9,
        description = ram3.ram_name,
        quantity = 20,
        product_type = ram3.ram_type,
        price = ram3.price,
        ram_id = ram3.ram_id
    )
    db.session.add(product9)
    db.session.commit()
    

    product10 = Product(
        product_id = 10,
        description = motherboard1.motherboard_name,
        quantity = 11,
        product_type = motherboard1.motherboard_type,
        price = motherboard1.price,
        motherboard_id = motherboard1.motherboard_id
    )
    db.session.add(product10)

    product11 = Product(
        product_id = 11,
        description = motherboard2.motherboard_name,
        quantity = 7,
        product_type = motherboard2.motherboard_type,
        price = motherboard2.price,
        motherboard_id = motherboard2.motherboard_id
    )
    db.session.add(product11)

    product12 = Product(
        product_id = 12,
        description = motherboard3.motherboard_name,
        quantity = 25,
        product_type = motherboard3.motherboard_type,
        price = motherboard3.price,
        motherboard_id = motherboard3.motherboard_id
    )
    db.session.add(product12)

    product13 = Product(
        product_id = 13,
        description = cpu3.cpu_name,
        quantity = 50,
        product_type = cpu3.cpu_type,
        price = cpu3.price,
        cpu_id = cpu3.cpu_id
    )
    db.session.add(product13)

    product14 = Product(
        product_id = 14,
        description = cpu4.cpu_name,
        quantity = 33,
        product_type = cpu4.cpu_type,
        price = cpu4.price,
        cpu_id = cpu4.cpu_id
    )
    db.session.add(product14)
    db.session.commit()

    compat1 = Compat(
        compat_id = 1,
        compatible = "Compatible",
        cpu_rating = cpu1.rating,
        motherboard_rating =motherboard1.rating,
        cpu_id = cpu1.cpu_id,
        motherboard_id = motherboard1.motherboard_id,
        cpu_name = cpu1.cpu_name,
        motherboard_name = motherboard1.motherboard_name
    )
    db.session.add(compat1)
    db.session.commit()

    compat2 = Compat(
        compat_id = 2,
        compatible = "Compatible",
        cpu_rating = cpu2.rating,
        motherboard_rating = motherboard2.rating,
        cpu_id = cpu2.cpu_id,
        motherboard_id = motherboard2.motherboard_id,
        cpu_name = cpu2.cpu_name,
        motherboard_name = motherboard2.motherboard_name
    )
    db.session.add(compat2)
    db.session.commit()
    
    compat3 = Compat(
        compat_id = 3,
        compatible = "Compatible",
        cpu_rating = cpu3.rating,
        motherboard_rating = motherboard3.rating,
        cpu_id = cpu3.cpu_id,
        motherboard_id = motherboard3.motherboard_id,
        cpu_name = cpu3.cpu_name,
        motherboard_name = motherboard3.motherboard_name
    )
    db.session.add(compat3)
    db.session.commit()
    #!-----------------------------------------RATINGS----------------------------------------------------!#

    rating1 = Ratings(
        rating_id = 1,
        product_id = product1.product_id,
        customer_id = customer1.customers_id,
        customer_name = customer1.first_name + " " + customer1.last_name,
        product_name = product1.description,
        rating = cpu1.rating,
        comment = "Great CPU, reasonable price.",
        price = cpu1.price
    )
    db.session.add(rating1)
    
    rating2 = Ratings(
        rating_id = 2,
        product_id = product2.product_id,
        customer_id = customer2.customers_id,
        customer_name = customer2.first_name + " " + customer2.last_name,
        product_name = product2.description,
        rating = cpu2.rating,
        comment = "This was an awesome upgrade from my last cpu. Would reccomend!",
        price = cpu2.price,
    )
    db.session.add(rating2)
    db.session.commit()

    rating3 = Ratings(
        rating_id = 3,
        product_id = 10,
        customer_id = customer3.customers_id,
        customer_name = customer3.first_name + " " + customer3.last_name,
        product_name = product10.description,
        rating = motherboard1.rating,
        comment = "Powerful motherboard, so much faster than the old one i just had!",
        price = product11.price
    )
    db.session.add(rating3)

    rating4 = Ratings(
        rating_id = 4,
        product_id = 5,
        customer_id = customer3.customers_id,
        customer_name = customer3.first_name + " " + customer3.last_name,
        product_name = product5.description,
        rating = psu1.rating,
        comment = "Recently upgraded my graphics card, needed a better PSU, this is the one!!!",
        price = product5.price
    )
    db.session.add(rating4)
    db.session.commit()

    print('Table seeded')