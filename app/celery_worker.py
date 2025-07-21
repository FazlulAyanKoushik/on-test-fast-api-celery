from celery import Celery
from celery.schedules import crontab

celery = Celery(
    __name__,
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

@celery.task
def create_task():
    print("Hi, I'm from celery")

# celery.conf.beat_schedule = {
#     'add-every-minute': {
#         'task': 'app.celery_worker.create_task',
#         'schedule': crontab(minute='*/1'),
#     },
# }

# How to run in evry 30 seconds
celery.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'app.celery_worker.create_task',
        'schedule': 30.0,
    },
}
celery.conf.timezone = 'UTC'
