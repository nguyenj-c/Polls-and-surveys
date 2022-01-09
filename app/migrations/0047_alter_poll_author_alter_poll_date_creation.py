# Generated by Django 4.0.2 on 2022-02-01 21:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0046_alter_poll_author_alter_poll_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='poll',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 1, 21, 31, 17, 289868, tzinfo=utc), verbose_name='date creation'),
        ),
    ]
