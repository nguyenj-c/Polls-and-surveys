# Generated by Django 4.0.1 on 2022-01-11 16:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_polls_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polls',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 11, 17, 38, 5, 121597), verbose_name='date creation'),
        ),
    ]