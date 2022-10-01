from flask import Blueprint 
from flask import request
from main import db
from main import bcrypt
from marshmallow.exceptions import ValidationError
from flask_jwt_extended import create_access_token
from datetime import timedelta
from models.admin import Administrator 
from schemas.admin_schema import admin_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

#! this controller is used for the administators, in this controller, admin passwords are hashed for security purposes, creating a new admin has constraints on email and password originality


admin = Blueprint('admin', __name__, url_prefix='/admin')


#! THIS LOGIN HAS BEEN CODED JUST TO SHOW I COULD DO IT, I INTEND ON USING THIS API USING ONLY 1 ADMIN (CHRIS), TO LOG IN TO THIS ADMIN AND ACCESS THE TOKEN, FIND THE HARD CODED PASSWORD IN COMMMANDS.PY. IT IS IN THE FIRST INSTANCE FOR THE SEED COMMAND. LINE 43.
@admin.route('/register', methods=['POST'])
def register_admin():
    register_fields = admin_schema.load(request.json)
    #check if admin is already registered
    admin = Administrator.query.filter_by(username = register_fields['username']).first()
    if admin:
        return {"Error": "That username is already registered. Administrators must be unique. Change register details and try again."}
    admin = Administrator.query.filter_by(email = register_fields['email']).first()
    if admin:
        return {"Error": "That email is already registered. Administrators must be unique. Change register details and try again."}
    admin = Administrator(
        username = register_fields['username'],
        email = register_fields['email'],
        password = bcrypt.generate_password_hash(register_fields['password']).decode('utf-8'))
    db.session.add(admin)
    db.session.commit()
    #generating a token, setting the identity (set as admin id) and expiration time (set as 5 days).
    token = create_access_token(identity = str(admin.admin_id), expires_delta=timedelta(days=5))
    return {"username": admin.username, "token": token}, 201

#DELETE administrator
@admin.route('/<int:id>', methods = ['DELETE'])
@jwt_required()
def delete_admin(id):
    #having trouble with the tokens at the moment, will need to rework
    # if get_jwt_identity() != 'admin':
    #     return {"DENIED": "You do not have permission to delete, only an administrator can delete. If you are an administrator, check your token and try again."}, 403
    admin = Administrator.query.get(id)
    if not admin:
        return {"Error":"No admin with that ID, change ID and try again."}
    db.session.delete(admin)
    db.session.commit()
    return{"Message": "Successfully delete ADMIN."}

#make a login for administrator 
#! LOGIN for admin
@admin.route('/login', methods = ['POST'])
def log_in():
    admin_fields = admin_schema.load(request.json)
    #filter_by returns a list, we just want the first element so we add .first 
    admin = Administrator.query.filter_by(username=admin_fields['username']).first()
    if not admin:
        return {"Error": "Username is invalid, change it and try again."}, 404
    if not bcrypt.check_password_hash(admin.password, admin_fields['password']):
        return {"Error": "Password is incorrect, change it and try again."}, 404

    token = create_access_token(identity = "admin", expires_delta=timedelta(days=5))
    
    return {"username": admin.username, "token": token}


@admin.errorhandler(ValidationError)
def register_validation_errors(error):
    return error.messages, 400
