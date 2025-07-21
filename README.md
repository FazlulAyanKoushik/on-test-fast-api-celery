# FastAPI + Celery Background Email Sender

## Project Overview

This project demonstrates how to use Celery with FastAPI for handling background tasks, specifically for sending emails. Celery is a robust distributed task queue that is more powerful and reliable than FastAPI's built-in BackgroundTasks, especially for long-running or resource-intensive operations. By using Celery, tasks are processed outside the main FastAPI process, allowing for better scalability and fault tolerance.

The email sending functionality is implemented as a Celery background task, which helps avoid issues with spam detection and ensures reliable delivery—similar to Django's email system. The project is configured to use Gmail's SMTP server with industry best practices (port 587 and STARTTLS), and all email settings are managed in a dedicated configuration file for clarity and security.

This setup is ideal for production-grade applications that require robust background processing and reliable email delivery.

## How to run
1. Run the service using docker:
    ```
    docker-compose up --build
    ```

Now, if you go to `http://localhost:8000/` you will see a message that the task is running in the background. You can also see the celery worker logs in the console.
