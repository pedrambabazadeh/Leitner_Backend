from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, set_access_cookies, unset_jwt_cookies, current_user

from ..extensions import db
from ..models import User
from ..services import AuthService

service = AuthService()

auth_bp = Blueprint('auth', __name__)
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')
    last_name = data.get('last_name')
    if not email or not password or len(password) < 8:
        return jsonify({'message': 'Please provide your email and password'}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already registered'}), 409
    hashed = generate_password_hash(password)
    user = service.register_user(name, last_name, email, hashed)
    resp = jsonify({'message': 'user created'})
    access_token = create_access_token(identity=user.id)
    set_access_cookies(resp, access_token)
    return resp, 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Please provide your valid email and password'}), 400
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'message': 'Invalid password'}), 401
    access_token = create_access_token(identity=str(user.id))
    resp = jsonify({'message': 'user logged in'})
    set_access_cookies(resp, access_token)
    return resp, 200
@auth_bp.route('/me', methods=['POST'])
@jwt_required()
def me():
    #print("🔍 Incoming cookies:", request.cookies)
    #print("🔍 JWT Identity:", get_jwt_identity())
    user_id = get_jwt_identity()
    user = User.query.get(int(user_id))
    if not user:
        return jsonify({'message': 'user not found'}), 404
    return jsonify({'id': user.id, 'email': user.email, 'name': user.name, 'last_name': user.last_name})

@auth_bp.route('/logout', methods=['POST'])
def logout():
    resp = jsonify({'message': 'user logged out'})
    unset_jwt_cookies(resp)
    return resp
