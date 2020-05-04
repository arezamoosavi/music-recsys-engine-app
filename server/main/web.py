import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from resources import Recommend

flask_app = Flask(__name__)
api = Api(flask_app)

#set configs
flask_app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY','1nd2')



#endpoints
api.add_resource(Recommend, '/recommend/<string:song>/<string:artist>/<int:number>',
                            '/recommend/<string:song>/<int:number>',
                            '/recommend/<string:song>/<string:artist>',
                            '/recommend/<string:song>')
