# Generated by Django 4.0.1 on 2022-01-12 07:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_polls_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polls',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 12, 8, 10, 35, 752735), verbose_name='date creation'),
        ),
    ]
