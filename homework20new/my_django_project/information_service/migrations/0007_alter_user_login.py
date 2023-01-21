# Generated by Django 4.1.5 on 2023-01-10 15:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information_service', '0006_alter_user_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(max_length=30, null=True, validators=[django.core.validators.RegexValidator(message='Логин должен начинаться с буквы и быть не больше 10 символов', regex='^[a-zA-Z]{6,10}$')]),
        ),
    ]
