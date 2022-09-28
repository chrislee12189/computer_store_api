from main import db 
#rating will be its own model later. will need to change to foreign key




class Product(db.Model):
    __tablename__ = 'product'
    product_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String())
    quantity = db.Column(db.Integer)
    product_type = db.Column(db.String())
    price = db.Column(db.Integer)
    cpus =db.relationship(
        #link the class 
        "Cpu",
        #back reference to this relationship is cpu
        backref="product"
    )
    motherboards=db.relationship(
        "Motherboards",
        backref="product"
    )