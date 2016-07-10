CELERY_IMPORTS = ('tasks')
CELERY_IGNORE_RESULT = False
BROKER_HOST = "127.0.0.1" #IP address of the server running RabbitMQ and Celery
BROKER_PORT = 5672
BROKER_URL='amqp://'
CELERY_RESULT_BACKEND = "amqp"
CELERY_IMPORTS=("tasks",)

from celery.schedules import crontab
from datetime import timedelta
 
CELERYBEAT_SCHEDULE = {
    'add-every-10-seconds': {
        'task': 'tasks.fav_doctor',
        'schedule': timedelta(seconds=10),
    },
}

