# Generated by Django 4.1.5 on 2023-01-28 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='games_amount',
            field=models.IntegerField(default=0, verbose_name='Колличество игр'),
        ),
    ]
