import logging
from flask_restful import Resource
from flask import jsonify, request

#loging
logging.basicConfig(filename='logfiles.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")


class Recommend(Resource):
    def get(self,song: str, artist:str=None, number:int=6):

        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            ipp_address=request.environ['REMOTE_ADDR']
        else:
            ipp_address=request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy
        
        retJson = {
            "ipp_address": ipp_address,
            "status":200,
            "song":song,
            "artist":artist,
            "number":number
             }
    
        return jsonify(retJson)