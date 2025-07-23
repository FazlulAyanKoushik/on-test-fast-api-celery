from fastapi import FastAPI
from .celery_worker import create_task, send_mail_task

app = FastAPI()

@app.get("/health")
def read_root():
    create_task.delay()
    return {"message": "Task is running in the background"}

@app.post("/send-mail")
def send_mail():
    send_mail_task.delay()
    return {"message": "Email is being sent in the background"}
