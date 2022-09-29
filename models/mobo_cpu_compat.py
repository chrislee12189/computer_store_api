# from main import db 


# class MoboCpuCompat(db.Model):
    # __tablename__ = 'mobocpucompat'
    # compatibility_id = db.Column(db.Integer, primary_key=True)
    # compatible = db.Column(db.String())
    # motherboard_type = db.Column(db.Integer, db.ForeignKey('motherboards.motherboard_type'))
    # cpu_type = db.Column(db.Integer, db.ForeignKey('cpu.cpu_type'))
    # mobo = db.relationship(
    #     "MoboCpuCompat",
    #     backref = "motherboards"
    # )
    # cpu = db.relationship(
    #     "MoboCpuCompat",
    #     backref = "cpu"
    # )