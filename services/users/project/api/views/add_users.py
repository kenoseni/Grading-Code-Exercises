from sqlalchemy import exc
from project.api.users import users_blueprint
from flask import jsonify, request
from project.api.models import User
from project.api.utils import authenticate, is_admin
from database import db


@users_blueprint.route('/users', methods=['POST'])
@authenticate
def add_user(resp):
    post_data = request.get_json()
    response_object = {
        'status': 'fail',
        'message': 'Invalid payload.'
    }
    if not is_admin(resp):
        response_object[
            'message'] = 'You do not have permission to do that.'
        return jsonify(response_object), 401
    if not post_data:
        return jsonify(response_object), 400
    username = post_data.get('username')
    email = post_data.get('email')
    password = post_data.get('password')

    try:
        user = User.query.filter_by(email=email).first()
        if not user:
            User(
                username=username, email=email, password=password).save()
            response_object['status'] = 'success'
            response_object['message'] = f'{email} was added!'
            return jsonify(response_object), 201
        else:
            response_object['message'] = 'Sorry. That email already exists.'
            return jsonify(response_object), 400
    except (exc.IntegrityError, ValueError):
        db.session.rollback()
        return (response_object), 400
