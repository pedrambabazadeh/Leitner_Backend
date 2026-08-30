from app import create_app
from app.extensions import db

# Important: import models so SQLAlchemy knows about them
from app.models.core import *

app = create_app()

with app.app_context():
    db.create_all()
    print("Database tables created successfully.")