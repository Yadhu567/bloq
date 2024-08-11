from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import app, db
from app.models import user_schema

@app.route('/register', methods=['POST','GET'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    user = {
        "username": data['username'],
        "email": data['email'],
        "password": hashed_password
    }
    db.users.insert_one(user)
    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = db.users.find_one({"username": data['username']})
    if user and check_password_hash(user['password'], data['password']):
        access_token = create_access_token(identity=str(user["_id"]))
        return jsonify(access_token=access_token)
    return jsonify({"message": "Invalid credentials"}), 401
