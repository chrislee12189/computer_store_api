from main import db 

#! need to work on how this model will work. the intent is that it will link to customers via foreign key. price column needs to be worked on, i think it will end up being set up once in the products table and then referenced via foreign key. not sure yet.
class Ratings(db.Model):
    __tablename__ = 'ratings'
    rating_id = db.Column(db.Integer, primary_key=True)
    test = db.Column(db.String())
    # product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    # customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    # price = db.Column(db.Integer, db.ForeignKey('product.price'))