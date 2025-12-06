from ..services import UserService
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

service = UserService()

user_bp = Blueprint('user', __name__)

@user_bp.route('/info', methods=['GET'])
@jwt_required()
def info():
    user_id = get_jwt_identity()
    identity_number = int(user_id)
    user = service.get_user(identity_number)
    print(user.status)
    return user

