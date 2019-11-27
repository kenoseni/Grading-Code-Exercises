from sqlalchemy import exc
from project.api.users import users_blueprint
from flask import Blueprint, jsonify, request
from project.api.models import User
from database import db

@users_blueprint.route('/users', methods=['POST'])
def add_user():
    post_data = request.get_json()
    username = post_data.get('username')
    email = post_data.get('email')

    try:
        user = User.query.filter_by(email=email).first()
        if not user:
            new_user = User(username=username, email=email).save()
            response_object = {
                'status': 'success',
                'message': f'{email} was added!',
                'data': {
                    'id': new_user.id
                }
            }
            return jsonify(response_object), 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Sorry. That email already exists.'
            }
            return jsonify(response_object), 400
    except exc.IntegrityError as e:
        db.session.rollback()
        return {
            'status': 'fail',
            'message': 'Invalid payload.'}, 400

