from main import db 
#rating will be its own model later. will need to change to foreign key
class Psu(db.Model):
    __tablename__ = 'psu'
    psu_id = db.Column(db.Integer, primary_key=True)
    psu_type = db.Column(db.Integer)
    psu_name = db.Column(db.String())
    voltage = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    price = db.Column(db.Integer)
    product = db.relationship(
        "Product",#class im referencing
        backref = "psu"# this name can be any, the purpose of this is to use this as a field in the product schema, so make sure it matches with that field, cpu in both would make sense
    )