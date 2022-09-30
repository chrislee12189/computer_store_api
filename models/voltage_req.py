from main import db 

class VoltageReq(db.Model):
    __tablename__ = 'voltages'
    voltage_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
    gpu_id= db.Column(db.Integer, db.ForeignKey('gpu.gpu_id'))
    psu_id = db.Column(db.Integer, db.ForeignKey('psu.psu_id'))
    gpu_name = db.Column(db.String())
    psu_name = db.Column(db.String())
    voltage_req = db.Column(db.Integer)
    voltage_supplied = db.Column(db.Integer)
    comment = db.Column(db.String())

    #need to check if voltage references work as intended.
    #foreign key function here is supposed to check voltage needed against the voltage we have available.

