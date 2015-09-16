# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0009_auto_20150907_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('video_url', models.URLField()),
                ('zipped_submission', models.FileField(upload_to=b'')),
                ('description', models.TextField(help_text=b"Any last-minute comments? Don't forget you should have a README!", blank=True, validators=[django.core.validators.MaxLengthValidator(1000)])),
                ('team', models.ForeignKey(to='teams.Team')),
            ],
            options={
                'ordering': ['created'],
                'get_latest_by': 'created',
            },
        ),
    ]
