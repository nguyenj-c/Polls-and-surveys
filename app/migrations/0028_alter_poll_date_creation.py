# Generated by Django 4.0.1 on 2022-01-18 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_alter_poll_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 18, 15, 4, 2, 568729), verbose_name='date creation'),
        ),
    ]
