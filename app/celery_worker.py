from celery import Celery
from celery.schedules import crontab

from app.email_settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_RECIPIENTS, EMAIL_SUBJECT, EMAIL_BODY

celery = Celery(
    __name__,
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

import smtplib
from email.message import EmailMessage
import email.utils

@celery.task
def create_task():
    print("Hi, I'm from celery")

@celery.task
def send_mail_task():
    msg = EmailMessage()
    msg["From"] = EMAIL_HOST_USER
    msg["To"] = ", ".join(EMAIL_RECIPIENTS)
    msg["Subject"] = EMAIL_SUBJECT
    msg["Date"] = email.utils.formatdate(localtime=True)
    msg["Message-ID"] = email.utils.make_msgid()
    msg["Reply-To"] = EMAIL_HOST_USER
    msg.set_content(EMAIL_BODY)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.send_message(msg, from_addr=EMAIL_HOST_USER, to_addrs=EMAIL_RECIPIENTS)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

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
