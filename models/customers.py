from main import db 

class Customer(db.Model):
    # Set the database table that will store instances of this model
    __tablename__ = 'customers'
    #define the columns and attributes needed 
    customers_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    address = db.Column(db.String())
    postcode = db.Column(db.Integer)
    phone = db.Column(db.Integer)