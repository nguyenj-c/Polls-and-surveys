# Generated by Django 4.0.1 on 2022-01-12 08:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_polls_date_creation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sujet', models.CharField(blank=True, max_length=200)),
                ('Question', models.CharField(blank=True, max_length=200, null=True)),
                ('date_creation', models.DateTimeField(default=datetime.datetime(2022, 1, 12, 9, 17, 50, 414315), verbose_name='date creation')),
            ],
        ),
        migrations.RemoveField(
            model_name='polls',
            name='Question',
        ),
        migrations.RemoveField(
            model_name='polls',
            name='Sujet',
        ),
        migrations.RemoveField(
            model_name='polls',
            name='date_creation',
        ),
        migrations.AddField(
            model_name='polls',
            name='option_1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='polls',
            name='option_1_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='polls',
            name='option_2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='polls',
            name='option_2_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='polls',
            name='option_3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='polls',
            name='option_3_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='polls',
            name='option_4',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='polls',
            name='option_4_count',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.AddField(
            model_name='polls',
            name='sujet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.subject'),
        ),
    ]
