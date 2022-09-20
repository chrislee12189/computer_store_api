from main import db 

#rating will be its own model later. will need to change to foreign key
class Motherboards(db.Model):
    __tablename__ = 'motherboards'
    motherboard_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    motherboard_type = db.Column(db.Integer)
    motherboard_name = db.Column(db.String())
    price = db.Column(db.Integer, db.ForeignKey('product.price'))
    rating = db.Column(db.Integer)
