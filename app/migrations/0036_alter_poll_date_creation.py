# Generated by Django 4.0.1 on 2022-01-19 12:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_alter_poll_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 19, 12, 9, 5, 146919), verbose_name='date creation'),
        ),
    ]