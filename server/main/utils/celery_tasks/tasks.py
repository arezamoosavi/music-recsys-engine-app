import logging
from utils.rec_handler import getMusic
from utils.celery_tasks.main_app import CELERY as c

async_recommend = c.task(getMusic)
