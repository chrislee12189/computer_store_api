from main import db


class Compat(db.Model):
    __tablename__ = 'compat'
    compat_id = db.Column(db.Integer, primary_key=True)
    compatible = db.Column(db.String())
    cpu_rating = db.Column(db.Integer)
    motherboard_rating = db.Column(db.Integer)
    cpu_id = db.Column(db.Integer, db.ForeignKey("cpu.cpu_id"))
    motherboard_id = db.Column(db.Integer, db.ForeignKey("motherboards.motherboard_id"))
    cpu_name = db.Column(db.String())
    motherboard_name = db.Column(db.String())