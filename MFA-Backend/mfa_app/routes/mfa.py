from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import User, db
from utils.security import get_grid_value
import json

mfa_bp = Blueprint("mfa", __name__)

@mfa_bp.route("/verify-grid", methods=["POST"])
def verify_grid():
    data = request.json

    if not data.get("username") or not data.get("answers"):
        return jsonify({"error": "Username and answers are required"}), 400

    user = User.query.filter_by(username=data["username"]).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    required_coords = json.loads(user.grid_coordinates)
    if any(coord not in data["answers"] for coord in required_coords):
        return jsonify({"error": "Missing answers for some coordinates"}), 400

    for coord in required_coords:
        expected_value = get_grid_value(coord)
        if data["answers"][coord] != expected_value:
            return jsonify({"error": "Invalid grid code"}), 401

    return jsonify({
        "msg": "MFA successful"
    }), 200
