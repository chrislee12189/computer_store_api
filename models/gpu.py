from main import db 

#rating will be its own model later. will need to change to foreign key
class Gpu(db.Model):
    __tablename__ = 'gpu'
    # product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    gpu_id = db.Column(db.Integer, primary_key=True)
    gpu_type = db.Column(db.Integer)
    gpu_name = db.Column(db.String())
    voltage_required = db.Column(db.Integer)
    price = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    product = db.relationship(
        "Product", #class im referencing
        backref = "gpu"
        # this name can be any, the purpose of this is to use this as a field in the product schema, so make sure it matches with that field
    )
    