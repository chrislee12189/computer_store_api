from main import db 
#rating will be its own model later. will need to change to foreign key




class Product(db.Model):
    __tablename__ = 'product'
    product_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String())
    quantity = db.Column(db.Integer)
    product_type = db.Column(db.String())
    price = db.Column(db.Integer)
    cpu_id = db.Column(db.Integer, db.ForeignKey("cpu.cpu_id"))
    gpu_id = db.Column(db.Integer, db.ForeignKey("gpu.gpu_id"))
    psu_id = db.Column(db.Integer, db.ForeignKey("psu.psu_id"))
    ram_id = db.Column(db.Integer, db.ForeignKey("ram.ram_id"))
    motherboard_id = db.Column(db.Integer, db.ForeignKey("motherboards.motherboard_id"))