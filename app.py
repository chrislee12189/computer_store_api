#use flask for db, use jsonify for jsonifying database relations, use marshmallow for converting models/objects into json, use sqlalchemy to create models
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 


#create new flask app, name = 'app'
app = Flask(__name__)
#SQLAlchemy constructor to connect to database. URI tells it which database to connect to.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://computer_store_user:123456@localhost:5432/computer_store_db"


db = SQLAlchemy(app)
ma = Marshmallow(app)

#schema defines what the structure of our data is so that when we go to convert to json, it knows how to work/which of the columns we want included
#schema tells marshmallow which fields we want included in our json
class CustomerSchema(ma.Schema):
    #declare subclass, must be named Meta. required by ms.Schema, if we dont declare this it will not work.
    class Meta:
        #list inside the tuple states which field we want in our json
        fields = ('id', 'first_name', 'last_name', 'address', 'postcode', 'phone')

#define user model
class Customer(db.Model):
    # Set the database table that will store instances of this model
    __tablename__ = 'customers'
    #define the columns and attributes needed 
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    address = db.Column(db.String())
    postcode = db.Column(db.Integer)
    phone = db.Column(db.Integer)
    
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
    #same as sql select * from users; get all customers from database table
    customers = Customer.query.all()
    #convert the cards from the database into a JSON format and store them in the result variable
    result = CustomerSchema(many=True).dump(customers)
    #return the data in json format
    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True)