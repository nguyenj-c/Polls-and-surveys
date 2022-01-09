# Generated by Django 3.2.9 on 2022-01-30 19:51

import app.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0040_auto_20220130_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='poll',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 30, 19, 51, 13, 808666, tzinfo=utc), verbose_name='date creation'),
        ),
    ]
