from flask import Blueprint, request, jsonify
from app.extensions import db
from sqlalchemy.orm import joinedload
from app.models import User

class AuthService:
    def register_user(self, name, last_name, email, hashed_password):
        user = User(name= name, last_name=last_name, email=email, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        return user