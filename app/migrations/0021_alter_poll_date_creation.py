# Generated by Django 4.0.1 on 2022-01-13 21:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_poll_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 13, 22, 44, 55, 950035), verbose_name='date creation'),
        ),
    ]
