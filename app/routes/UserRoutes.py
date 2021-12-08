from flask import Blueprint, request, current_app, make_response, jsonify
from app.models.User import User
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
)

user_api = Blueprint('user_api', __name__, url_prefix="/user")


@user_api.route('/login', methods=['POST'])
def login():
    user_dto = request.get_json()
    print(user_dto)
    user = User.query.filter_by(username=user_dto.get('username')).first()
    if not user:
        return make_response(jsonify({'message': 'User doesnt exitst'})), 401
    if User.verify_hash(user_dto.get('password'), user.password):
        access_token = create_access_token(identity=user.username)
        return make_response(jsonify({"x-access-token": access_token})), 200
    else:
        return make_response(jsonify({'message': 'Wrong credentials'})), 401


@user_api.route('/create', methods=['POST'])
def create_new_user():
    user_dto = request.get_json()
    user = User.query.filter_by(username=user_dto.get('username')).first()
    if not user:
        user = User(username=user_dto.get('username', None), password=User.generate_hash(user_dto.get('password')))
        try:
            user.save()
            access_token = create_access_token(identity=user.username)
            return make_response(jsonify({'x-access-token': access_token}))
        except Exception as e:
            return make_response(jsonify({'message': 'Some error occurred. Please try again.'})), 401
    else:
        return make_response(jsonify({'message': 'User already exists. Please Log in.', })), 202


@user_api.route('/ping', methods=['GET'])
@jwt_required()
def ping():
    return "ping"
