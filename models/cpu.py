from main import db 
#rating will be its own model later. will need to change to foreign key
class Cpu(db.Model):
    __tablename__ = 'cpu'
    cpu_id = db.Column(db.Integer, primary_key=True)
    # product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    cpu_type = db.Column(db.Integer)
    cpu_name = db.Column(db.String())
    price = db.Column(db.Integer)
    rating = db.Column(db.Integer)