import logging
from flask_restful import Resource
from flask import jsonify, request, json, make_response, url_for
from functools import wraps
from auth.models import UserModel
from flask_login import login_user, current_user, logout_user, login_required


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

            user = UserModel.find_by_username(username=username)
            # user = UserModel.get_or_create(username=username,password=password)
            if user & user.check_password(password=password):

                login_user(user)
                return f(*args, **kwargs)
            else:
                return make_response(url_for('login'))
        
        return make_response('First Login!',401, {'WWW-Authenticate' : 'Basic realm="Login req"'})
    
    return decorated


class Login(Resource):

    def get(self, username, password):
            user = UserModel.get_or_create(username=username,password=password)
            login_user(user)
            return 'You are logged in as {}'.format(current_user.username)

class Logout(Resource):

    @login_required
    def get(self):
        logout_user()
        return 'You are Loged out Successfully!'
