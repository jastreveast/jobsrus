from flask import Blueprint, request, jsonify, make_response, current_app as app
from application.database import db
from application.models.user import User
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from .auth_decorators import token_required


auth_bp = Blueprint(
    'auth_bp',
    __name__,
   
)

@auth_bp.route('/user', methods=['POST'])
def create_user():
    # get user information
    json = request.get_json()
    username = json.get('username')
    password = json.get('password')

    hashed_password = generate_password_hash(password, method='sha256')

    new_user = User(public_id=str(uuid.uuid4()), username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'new user created'}), 200 

@auth_bp.route('/login', methods=['POST'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('could not verify', 401, {'WWW-Authenticate': 'basic realm="login required!"'})

    user = User.query.filter(User.username==auth.username).first()

    if not user:
        return make_response('could not verify', 401, {'WWW-Authenticate': 'basic realm="login required!"'})
    
    if check_password_hash(user.password, auth.password):
        token = jwt.encode({
            'public_id' : user.public_id,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
            app.config['SECRET_KEY'])
        
        return jsonify({'token' : token.decode('UTF-8')})
    
    return make_response('could not verify', 401, {'WWW-Authenticate': 'basic realm="login required!"'})

@auth_bp.route('/profile', methods=['GET'])
@token_required
def profile(current_user):
    return jsonify({'message' : 'all users profile information here'}), 200
