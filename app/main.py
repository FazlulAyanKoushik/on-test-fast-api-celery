from fastapi import FastAPI
from .celery_worker import create_task

app = FastAPI()

@app.get("/")
def read_root():
    create_task.delay()
    return {"message": "Task is running in the background"}
