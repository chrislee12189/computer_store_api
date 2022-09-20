from main import db 

class Ram(db.Model):
    __tablename__ = 'ram'
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    ram_type = db.Column(db.Integer)
    ram_name = db.Column(db.String())
    price = db.Column(db.Intger)
    rating = db.Column(db.Integer)
    