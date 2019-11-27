from sqlalchemy import exc
from project.api.users import users_blueprint
from flask import Blueprint, jsonify, request
from project.api.models import User
from database import db

@users_blueprint.route('/users/<user_id>', methods=['GET'])
def get_single_user(user_id):
    """Get Single user details"""
    user =  User.query.filter_by(id=user_id).first()
    response_object = {
        'status': 'success',
        'data': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'active': user.active
        }
    }
    return jsonify(response_object), 200
    