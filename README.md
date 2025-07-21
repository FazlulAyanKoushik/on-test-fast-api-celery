# Test Fast API Celery

This is a simple project to test Celery working with FastAPI. The project is dockerized.

## How to run
1. Run the services:
    ```
    docker-compose up --build
    ```

Now, if you go to `http://localhost:8000/` you will see a message that the task is running in the background. You can also see the celery worker logs in the console.