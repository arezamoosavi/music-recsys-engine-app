from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

REDIS_URL = os.environ.get('REDIS_URL','redis://redis:6379/0')
BROKER_URL = os.environ.get('RMQ_URL','amqp://admin:mypass@rabbitmq:5672')
BACKEND = 'rpc://'

CELERY = Celery('tcelery',
                broker=BROKER_URL,
                backend=REDIS_URL,
                include=['utils.celery_tasks.tasks']
                )