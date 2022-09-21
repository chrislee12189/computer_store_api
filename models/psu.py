from main import db 
#rating will be its own model later. will need to change to foreign key
class Psu(db.Model):
    __tablename__ = 'psu'
    psu_id = db.Column(db.Integer, primary_key=True)
    # product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    psu_type = db.Column(db.Integer)
    psu_name = db.Column(db.String())
    voltage = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    # price = db.Column(db.Integer, db.ForeignKey('product.price'))