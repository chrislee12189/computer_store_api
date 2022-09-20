from main import db 

class GpuPsuCompat(db.Model):
    __tablename__ = 'GpuPsuCompat'
    voltage_compatablity_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    gpu_type = db.Column(db.Integer, db.ForeignKey('gpu.type'))
    psu_type = db.Column(db.Integer, db.ForeignKey('psu.type'))
    voltage_needed = db.Column(db.Integer, db.ForeignKey('gpu.voltage_required'))
    voltage_present = db.Column(db.Integer, db.ForeignKey('psu.voltage'))


    #need to check if voltage references work as intended.
    #foreign key function here is supposed to check voltage needed against the voltage we have available.

