from models import db
from app import create_app  # import the factory, not app()

app = create_app()

with app.app_context():
    db.drop_all()   # ⚠️ this will erase all data
    db.create_all()
    print("✅ Database has been reset and all tables created.")
