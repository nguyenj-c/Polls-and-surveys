# Generated by Django 4.0.1 on 2022-01-18 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_alter_poll_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 18, 15, 7, 36, 972288), verbose_name='date creation'),
        ),
    ]
