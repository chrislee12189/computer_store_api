from main import db 


class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True)
    customers_id = db.Column(db.Integer,db.ForeignKey('customers.customers_id'), nullable=False)
    customer_name = db.Column(db.String())
    to_address = db.Column(db.String())
    to_postcode = db.Column(db.Integer)
    shipping_date = db.Column(db.Integer)

