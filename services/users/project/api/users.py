"""Users Blueprint"""
from flask import Blueprint, jsonify, render_template, request
from project.api.models import User

users_blueprint = Blueprint('users', __name__, template_folder='./templates')

@users_blueprint.route('/users/ping')
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong'
    })

@users_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        User(username=username, email=email).save()
    users = User.query.all()
    return render_template('index.html', users=users)
