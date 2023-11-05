import logging

from datetime import timedelta

from core.celery import celery_app

from currencies.utils import update_currency_rates

logger = logging.getLogger("django")


@celery_app.task(name="update_currency_task")
def update_currency():
    update_currency_rates()


celery_app.conf.beat_schedule = {
    # Executes every RUN_EVERY_MINUTE minutes
    "update-currency-every-5-minutes": {
        "task": "update_currency_task",
        "schedule": timedelta(minutes=5),
    },
}
