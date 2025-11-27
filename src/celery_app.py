# src/celery_app.py

import os

from celery import Celery  # type: ignore

# ---------------------------------------------------------------------
# Load environment variables for broker and backend
# Celery will use Redis (recommended for your architecture)
# ---------------------------------------------------------------------
REDIS_URL = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/1")

# ---------------------------------------------------------------------
# Create Celery instance
# ---------------------------------------------------------------------
celery = Celery(
    "aicontent",
    broker=REDIS_URL,
    backend=RESULT_BACKEND,
    include=["src.tasks"],  # auto-load all tasks from tasks.py
)

# ---------------------------------------------------------------------
# Celery Configuration
# ---------------------------------------------------------------------
celery.conf.update(
    broker_connection_retry_on_startup=True,
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)
