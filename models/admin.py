from main import db 

#! username and email must be unique when creating an admin. 
class Administrator(db.Model):
        __tablename__ = 'admin'
        admin_id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(), nullable=False, unique=True)
        email = db.Column(db.String(), nullable=False, unique=True)
        password = db.Column(db.String(), nullable=False)