# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import project.submission.models
import django.core.validators
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0009_auto_20150907_1920'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FileSubmission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('submission', models.FileField(upload_to=project.submission.models.get_file_dir)),
                ('comments', models.TextField(help_text=b"Any last-minute comments? Don't forget you need README!", blank=True, validators=[django.core.validators.MaxLengthValidator(1000)])),
                ('md5sum', models.CharField(max_length=32, blank=True)),
                ('submitter', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='teams.Team', null=True)),
            ],
            options={
                'ordering': ['-created'],
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='VideoSubmission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('video_url', models.URLField()),
                ('submitter', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='teams.Team', null=True)),
            ],
            options={
                'ordering': ['-created'],
                'get_latest_by': 'created',
            },
        ),
    ]
