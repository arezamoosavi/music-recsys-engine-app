import logging
from flask_restful import Resource
from flask import jsonify, request, json, make_response
from functools import wraps
from auth.models import UserModel
from flask_login import login_user, current_user, logout_user


#loging
logging.basicConfig(filename='logfiles.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")


"""def basic_authenticator(f):
        @wraps(f)
        def authenticate(*args, **kwargs):
            logging.info('In wrapped function')
            username = request.authorization['username']
            password = request.authorization['password']
            is_valid = True if username == password else False
            if not is_valid:
                logging.error('[Authentication] [User-{}] tried to access '
                                 '[path-{}] with [password-{}]'
                                 .format(username, request.path, password))
                return jsonify({
                    'message': 'Username and password must be same.'
                })
            return f(*args, **kwargs)
        return authenticate"""


def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth:
            username = auth.username
            password = auth.password

            user = UserModel.get_or_create(username=username,password=password)
            if user.check_password(password=password):

                login_user(user)

                return f(*args, **kwargs)
        
        return make_response('First Login!',401, {'WWW-Authenticate' : 'Basic realm="Login req"'})
    
    return decorated


class Login(Resource):

    @auth_required
    def get(self):
        return 'You are Loged in Successfully!'

class Logout(Resource):

    def get(self):
        user = current_user.user
        logout_user(user)
        return 'You are Loged out Successfully!'
