
from flask import Blueprint, request, jsonify
from models import User, db
from utils.security import hash_password, check_password, generate_coordinates
import json

auth_bp = Blueprint("auth", __name__)

# REGISTER
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username,  password = data.get("username"),  data.get("password")

    # Username and password are required; email is optional
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    # Check if username already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 400

    # If email is provided, check uniqueness
    #if email and User.query.filter_by(email=email).first():
        #return jsonify({"error": "Email already exists"}), 400

    coords = generate_coordinates(3)
    new_user = User(
        username=username,
        #email=email if email else None,  # Store None if not provided
        password_hash=hash_password(password),
        grid_coordinates=json.dumps(coords)
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "Registered successfully", "assigned_coordinates": coords}), 201

# LOGIN (Step 1 - password check only)
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username, password = data.get("username"), data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    user = User.query.filter_by(username=username).first()
    if not user or not check_password(password, user.password_hash):
        return jsonify({"error": "Invalid credentials"}), 401

    coords = json.loads(user.grid_coordinates)
    return jsonify({"msg": "Password correct, verify MFA", "required_coordinates": coords}), 200
