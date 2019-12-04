from project.api.users import users_blueprint
from flask import jsonify
from project.api.models import User


@users_blueprint.route('/users', methods=['GET'])
def get_all_user():
    """Get all users"""
    response_object = {
        'status': 'success',
        'data': {
            'users': [user.to_json() for user in User.query.all()]
        }
    }
    return jsonify(response_object), 200
