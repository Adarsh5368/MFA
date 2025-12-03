from flask import Blueprint, request, jsonify
from models import User, db
from flask_jwt_extended import create_access_token
from utils.face_utils import train_face_model, verify_face_model

face_bp = Blueprint("face_bp", __name__)

@face_bp.route("/enroll", methods=["POST"])
def enroll_face():
    username = request.form.get("username")
    file = request.files.get("file")

    if not username or not file:
        return jsonify({"msg": "Missing username or file"}), 400

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"msg": "User not found"}), 404

    model_bytes, err = train_face_model(file.read())
    if err:
        return jsonify({"msg": err}), 400

    user.face_model = model_bytes
    db.session.commit()
    return jsonify({"msg": "Face enrolled successfully", "username": username}), 200


@face_bp.route("/verify", methods=["POST"])
def verify_face():
    username = request.form.get("username")
    file = request.files.get("file")

    if not username or not file:
        return jsonify({"msg": "Missing username or file"}), 400

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"msg": "User not found"}), 404

    if not user.face_model:
        return jsonify({"msg": "No face model enrolled"}), 400

    label, confidence, err = verify_face_model(user.face_model, file.read())
    if err:
        return jsonify({"msg": err}), 400

    if confidence <= 70:  # threshold for match
        token = create_access_token(identity=username)
        return jsonify({
            "msg": "Face verified",
            "username": username,
            "confidence": confidence,
            "token": token
        }), 200
    else:
        return jsonify({"msg": "Face not recognized", "confidence": confidence}), 401
