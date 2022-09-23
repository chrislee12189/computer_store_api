from main import db 

class Ram(db.Model):
    __tablename__ = 'ram'
    ram_id = db.Column(db.Integer, primary_key=True)
    # product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    ram_type =db.Column(db.String())
    ram_size = db.Column(db.Integer)
    ram_name = db.Column(db.String())
    price = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    