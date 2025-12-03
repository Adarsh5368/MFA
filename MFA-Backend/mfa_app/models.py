from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import json

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    #email = db.Column(db.String(120), unique=True, nullable=True)
    # Inside your User model class
    face_model = db.Column(db.LargeBinary, nullable=True)

    password_hash = db.Column(db.String(512), nullable=False)
    grid_coordinates = db.Column(db.String(255), nullable=False)  # JSON string of 3 coords

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_grid_coordinates(self, coords):
        self.grid_coordinates = json.dumps(coords)

    def get_grid_coordinates(self):
        return json.loads(self.grid_coordinates)
