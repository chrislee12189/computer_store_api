from flask import Blueprint 
from flask import jsonify
from flask import request
from main import db 
from models.product import Product 
from schemas.product_schema import product_schema, products_schema
from flask_jwt_extended import jwt_required

#! this controller is used for all products that will be present on databse. This will be a complete list of products that have been seperated by type in other tables.

#! products controller has more constraints than customer or orders. here only an admin can create, update or delete a product. I have done it like this because items available for customers/present in orders should be protected against anyone changing them or removing them. As for customer and orders, they are free to manage their own details.

products = Blueprint('products', __name__, url_prefix='/products')

#GET all products
@products.route('/', methods=['GET'])
def get_product():
    product_list = Product.query.all()
    result = products_schema.dump(product_list)
    return jsonify(result)

#GET 1 product
@products.route('/<int:id>', methods=['GET'])
def find_product(id):
    product_list = Product.query.get(id)
    result = products_schema.dump(product_list)
    return jsonify(result)

#CREATE product 
#! only available to admin
@products.route('/', methods=['POST'])
@jwt_required()
def create_product():
    product_fields = product_schema.load(request.json)
    product = Product(
        description=product_fields['description'],
        quantity=product_fields['quantity'],
        product_type=product_fields['product_type'],
        price = product_fields['price']
    )
    db.session.add(product)
    db.session.commit()
    return jsonify(product_schema.dump(product))

#UPDATE product
#! only available to admin
@products.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_product(id):
    product = Product.query.get(id)
    if not product:
        return {"Error": "Product does not exsist, in order to update a product, it must exists in the database."}
    product_fields = product_schema.load(request.json)
    product.description = product_fields['description']
    product.type= product_fields['type']
    product.price = product_fields['price']
    db.session.commit()
    return jsonify(product_schema.dump(product))
    
#DELETE product
#! only available to admin
@products.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_product(id):
    product = Product.query.get(id)
    if not product:
        return {"Error":"Cannot delete a product that does not exsist. Please enter a product that exsists."}
    db.session.delete(product)
    db.session.commit()
    return {"Message": "Product successfully deleted."}
