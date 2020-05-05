import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from resources import Recommend
from db import db, DATABASE_URI
from flask_migrate import Migrate

flask_app = Flask(__name__)
api = Api(flask_app)

#set configs
flask_app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY','1nd2')

#db setup
flask_app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('POSTGRES_URL', DATABASE_URI)
flask_app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(flask_app)
migrate = Migrate(flask_app, db)

@flask_app.before_first_request
def create_tables():
    db.create_all()


#endpoints
api.add_resource(Recommend, '/recommend/<string:song>/<string:artist>/<int:number>',
                            '/recommend/<string:song>/<int:number>',
                            '/recommend/<string:song>/<string:artist>',
                            '/recommend/<string:song>')
