# Generated by Django 4.0.1 on 2022-01-13 20:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_polls_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polls',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 13, 21, 22, 10, 147919), verbose_name='date creation'),
        ),
    ]
