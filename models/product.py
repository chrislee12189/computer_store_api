from main import db 
#rating will be its own model later. will need to change to foreign key
class Product(db.Model):
    __tablename__ = 'product'
    product_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    quantity = db.Column(db.Integer)
    product_type = db.Column(db.String())

