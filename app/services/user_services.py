from app.models import User
from flask import jsonify

class UserService:
    #try:
        def get_user(self, user_id) :
            user = User.query.get(user_id)
            return jsonify({"name": user.name, "email": user.email})
      #  except :
      #      return jsonify({'message': 'User Not Found'})