# Generated by Django 3.2.9 on 2022-02-01 14:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_alter_poll_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 1, 14, 16, 36, 969195, tzinfo=utc), verbose_name='date creation'),
        ),
    ]
