# Generated by Django 4.0.1 on 2022-01-11 16:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_polls_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polls',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 11, 17, 30, 53, 747973), verbose_name='date creation'),
        ),
    ]
