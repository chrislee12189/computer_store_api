from main import db 
#rating will be its own model later. will need to change to foreign key



class Cpu(db.Model):
    __tablename__ = 'cpu'
    cpu_id = db.Column(db.Integer, primary_key=True)
    cpu_type = db.Column(db.Integer)
    cpu_name = db.Column(db.String())
    price = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    product = db.relationship(
        "Product",#class im referencing
        backref ="cpu"# this name can be any, the purpose of this is to use this as a field in the product schema, so make sure it matches with that field, cpu in both would make sense
    )