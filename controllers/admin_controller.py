from flask import Blueprint 
from flask import jsonify
from flask import request
from main import db
from main import bcrypt
from main import jwt
from flask_jwt_extended import create_access_token
from datetime import timedelta
from models.admin import Administrator 
from schemas.admin_schema import admin_schema

#! this controller is used for the administators, in this controller, admin passwords are hashed for security purposes, creating a new admin has constraints on email and password originality


admin = Blueprint('admin', __name__, url_prefix='/admin')

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
    return {"username": admin.username, "token": token}

#DELETE administrator
@admin.route('/<int:id>', methods = ['DELETE'])
def delete_admin(id):
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
        return {"Error": "Username is invalid, change it and try again."}
    if not bcrypt.check_password_hash(admin.password, admin_fields['password']):
        return {"Error": "Password is incorrect, change it and try again."}

    token = create_access_token(identity = "admin", expires_delta=timedelta(days=5))
    
    return {"username": admin.username, "token": token}