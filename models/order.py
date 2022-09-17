from sqlalchemy import ForeignKey
from main import db 
from datetime import date

class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True)
    customers_id = db.Column(db.Integer, ForeignKey('customers.id'))
    customer_name = db.Column(db.String())
    to_address = db.Column(db.String())
    to_postcode = db.Column(db.Integer)
    shipping_date = db.Column(db.date.fromisoformat('2022-01-01'))

