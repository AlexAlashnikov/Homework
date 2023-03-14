import datetime
import logging

from better_profanity import profanity
from celery import shared_task
from django.contrib.auth.models import User
from django.core import serializers
from django.core.mail import send_mail

from game_store.models import Game


profanity.load_censor_words()

@shared_task()
def replace_text_with_censored(instance):
    instance = list(serializers.deserialize('json', instance))[0].object
    print(f"{instance.text} {instance.user}")
    censored_text = profanity.censor(instance.text)
    instance.text = censored_text
    instance.save()
    print(f"{instance.text} {instance.user}")


logger = logging.getLogger(__name__)


@shared_task()
def game_store_logger_info(getting_time, getting_path, getting_user):
    message = f"{getting_time} | {getting_path} | {getting_user}"
    logger.info(message)


@shared_task()
def send_news_email_task(games, user:dict):
    message_text = f'Hello {user["username"]}! Here are the top 3 games of this week!\n'
    for game in games:
        msg_chunk = f"Name: {game['name']};\n Release Date: {game['release_date']};\n Price:{game['price']}\n"
        message_text += msg_chunk
    send_mail(
            "Weekly Top Games!",
            message_text, "support@example.com",[user['email']],
            fail_silently=False,
            )


@shared_task()
def weekly_notification():
    all_users = list(User.objects.filter(is_staff=False).values())
    top_games = list(
                Game.objects.filter(
                pub_date__gte=datetime.datetime.today()-datetime.timedelta(days=70)).
                order_by('games__grade')[:3].values()
                )
    for user in all_users:
        send_news_email_task.delay(top_games, user)
