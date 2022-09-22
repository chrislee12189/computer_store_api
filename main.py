#use flask for db, use jsonify for jsonifying database relations, use marshmallow for converting models/objects into json, use sqlalchemy to create models
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 

app = Flask(__name__)    
app.config.from_object('config.app_config')
db = SQLAlchemy(app)
ma = Marshmallow(app)

def create_app():
    #create new flask app, name = 'app'
    db.init_app(app)
    ma.init_app(app)
    #begin modularisation of app so cli commands dont rely on 'app' prefix
    from commands import db_commands
    # register the blueprint for our commands. commands and controllers will use blueprints
    app.register_blueprint(db_commands)
    from controllers import registerable_controllers
    #iteration of controllers, map controllers 
    for controller in registerable_controllers:
        app.register_blueprint(controller)
    return app

#schema defines what the structure of our data is so that when we go to convert to json, it knows how to work/which of the columns we want included
#schema tells marshmallow which fields we want included in our json
class CustomerSchema(ma.Schema):
    #declare subclass, must be named Meta. required by ms.Schema, if we dont declare this it will not work.
    class Meta:
        #list inside the tuple states which field we want in our json
        fields = ('customers_id', 'first_name', 'last_name', 'address', 'postcode', 'phone')


#create models
@app.cli.command('create')
def create_db():
    # Tell SQLAlchemy to create all tables for all models in the physical database
    db.create_all()
    print('Tables created.')

@app.cli.command('drop')
def drop_db():
    #drop tables
    db.drop_all()
    print('Tables have been dropped successfully.')

@app.cli.command('seed')
def seed():
    from models.customers import Customer 
    customer = Customer(
        first_name = 'Chris',
        last_name = 'Lee',
        address = 'Main street, New York',
        postcode = '4567',
        phone = '0123456789'
    )
    #add new user to the current memory transaction (similar to git add)
    db.session.add(customer)
    # commit that transaction to the physical database (similar to git commit/push)
    db.session.commit()
    print('Table seeded successfully.')

#This route will respond to a 'get' request and return the string defined in the function
@app.route('/')
def index():
    return 'Test route works.'


@app.route('/customers')
def customer_route():
    from models.customers import Customer 
    #same as sql select * from users; get all customers from database table
    customers = Customer.query.all()
    #convert the cards from the database into a JSON format and store them in the result variable
    result = CustomerSchema(many=True).dump(customers)
    #return the data in json format
    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True)