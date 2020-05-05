import logging
from flask_restful import Resource
from flask import jsonify, request, json, make_response
from utils.rec_handler import getMusic
from utils.celery_tasks.tasks import async_recommend
from models import MusicModel
from schema import music_schema

#loging
logging.basicConfig(filename='logfiles.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")


class Recommend(Resource):
    def get(self,song: str, artist:str=None, number:int=6):

        # musics = getMusic(song=song, artist=artist, k=number)
        recTask = async_recommend.delay(song=song, artist=artist, k=number)
        musics = recTask.wait(timeout=None, interval=0.5)

        if musics:
            rec_success = True
        else:
            rec_success = False

        
        #save to db
        """try:
        except Exception as e:
                logging.error('Error! {}'.format(e))
                return "Could not Save", 400"""


        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            ip_address=request.environ['REMOTE_ADDR']
        else:
            ip_address=request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy
        
        #agent
        user_agent = request.user_agent.string

        new_musics = MusicModel(song=song, artist=artist, musics=musics, 
                                state=rec_success, ip=ip_address, agent=user_agent)
        try:
            new_musics.save_to_db()
        except:
            return {"message": ERROR_INSERTING}, 400
        
        retJson = {
            "ip_address": ip_address,
            "status":200,
            "musics": musics,
            "for": "music: {0}, artist: {1}".format(song, artist)
             }
    
        return jsonify(retJson)

class SearchHistory(Resource):
    def get(self):
        
        #get ip address
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            ip_address=request.environ['REMOTE_ADDR']
        else:
            ip_address=request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy

        search_res = MusicModel.find_by_ip(ip=ip_address)

        return jsonify({'data': [result.serialized for result in search_res]})
        # return music_schema.dump(search_res), 200