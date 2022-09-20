from main import db 

class MoboCpuCompat(db.Model):
    __tablename__ = 'MoboCpuCompat'
    compatibility_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    motherboard_type = db.Column(db.Integer, db.ForeignKey('motherboards.type'))
    cpu_type = db.Column(db.Integer, db.ForeignKey('cpu.type'))
    #voltage may not be necessary for this class. 
    voltage = db.Column(db.Integer)

