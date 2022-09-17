from main import db 


class Gpu(db.Model):
    __tablename__ = 'gpu'
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    gpu_type = db.Column(db.Integer)
    gpu_name = db.Column(db.String())
    voltage_required = db.Column(db.Integer)
    price = db.Column(db.Integer)
    rating = db.Column(db.Integer)