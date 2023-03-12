import logging
import time

from better_profanity import profanity
from celery import shared_task
from django.core import serializers


profanity.load_censor_words()

@shared_task()
def replace_text_with_censored(instance):
    instance = list(serializers.deserialize('json', instance))[0].object
    print(f"{instance.text} {instance.user}")
    censored_text = profanity.censor(instance.text)
    time.sleep(10)
    instance.text = censored_text
    instance.save()
    print(f"{instance.text} {instance.user}")


logger = logging.getLogger(__name__)


@shared_task()
def game_store_logger_info(getting_time, getting_path, getting_user):
    message = f"{getting_time} | {getting_path} | {getting_user}"
    logger.info(message)
