# Generated by Django 4.1.5 on 2023-02-05 12:10

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_store', '0004_remove_category_title_category_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Имя')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('grade', models.DecimalField(choices=[(Decimal('1.0'), '★☆☆☆☆ (1/5)'), (Decimal('2.0'), '★★☆☆☆ (2/5)'), (Decimal('3.0'), '★★★☆☆ (3/5)'), (Decimal('4.0'), '★★★★☆ (4/5)'), (Decimal('5.0'), '★★★★★ (5/5)')], decimal_places=1, max_digits=2, verbose_name='Оценка игры')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='game_store.game')),
            ],
            options={
                'ordering': ['pub_date'],
            },
        ),
    ]
