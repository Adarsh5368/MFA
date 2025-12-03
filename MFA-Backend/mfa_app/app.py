from flask import Flask, jsonify
from flask_cors import CORS
from models import db
from config import Config
from flask_jwt_extended import JWTManager  

# Import blueprints
from routes.auth import auth_bp
from routes.mfa import mfa_bp
from routes.face import face_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Enable CORS for frontend communication (allow all origins for dev)
    CORS(app, supports_credentials=True)

    # Initialize database
    try:
        db.init_app(app)
    except Exception as e:
        print(f"Database initialization error: {e}")

    # Initialize JWT
    try:
        JWTManager(app)
    except Exception as e:
        print(f"JWT initialization error: {e}")

    # Create tables
    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            print(f"Error creating tables: {e}")

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(mfa_bp, url_prefix="/mfa") #ye change
    app.register_blueprint(face_bp, url_prefix="/face")

    @app.route("/")
    def home():
        return {"msg": "MFA Application Running"}

    # Error handler for internal server errors
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal Server Error"}), 500

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=8000)
