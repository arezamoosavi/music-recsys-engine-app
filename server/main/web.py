import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from resources import Recommend, SearchHistory
from db import db, DATABASE_URI
from ma import ma
from flask_login import LoginManager, current_user
from flask_migrate import Migrate
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from models import MusicModel
from auth.resources import Login, Logout
from auth.models import UserModel, TokenModel


flask_app = Flask(__name__)
api = Api(flask_app)

#auth
login= LoginManager(flask_app)

@login.user_loader
def load_user(user_id):
    return UserModel.find_by_id(_id=user_id)


#set configs
flask_app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY','1nd2')

#db setup
flask_app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('POSTGRES_URL', DATABASE_URI)
flask_app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(flask_app)
ma.init_app(flask_app)

migrate = Migrate(flask_app, db)


@flask_app.before_first_request
def create_tables():
    db.create_all()

#admin setup
class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

admin = Admin(flask_app, index_view=MyAdminIndexView())
admin.add_view(MyModelView(MusicModel, db.session))
admin.add_view(MyModelView(UserModel, db.session))
admin.add_view(MyModelView(TokenModel, db.session))

#endpoints
api.add_resource(Recommend, '/recommend/<string:song>/<string:artist>/<int:number>',
                            '/recommend/<string:song>/<int:number>',
                            '/recommend/<string:song>/<string:artist>',
                            '/recommend/<string:song>')
api.add_resource(SearchHistory, '/')
api.add_resource(Login,'/login/<string:username>/<string:password>')
api.add_resource(Logout,'/logout')