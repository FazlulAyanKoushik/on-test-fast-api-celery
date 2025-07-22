from decouple import config

EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_RECIPIENTS = [
    "kf.ayan17@gmail.com",
    "jbc.nayeem@gmail.com",
    "ayon15-7527@diu.edu.bd"
]
EMAIL_SUBJECT = "Test Email from FastAPI Celery"
EMAIL_BODY = "This is a test email sent using FastAPI and Celery."
