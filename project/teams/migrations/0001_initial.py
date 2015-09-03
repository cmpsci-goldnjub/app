# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created'],
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('slug', models.SlugField(serialize=False, primary_key=True)),
                ('name', models.CharField(help_text=b"Your team's project name!", max_length=50, validators=[django.core.validators.RegexValidator(regex=b'[\\w\\-.:\\s]+', message=b'Names can contain letters, numbers, dashes, periods, colons, and whitespace.')])),
                ('description', models.TextField(help_text=b"Tell us about your project! Or don't. It's up to you!", blank=True)),
                ('rendered_description', models.TextField(editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
                'get_latest_by': 'created',
            },
        ),
        migrations.AddField(
            model_name='request',
            name='team',
            field=models.ForeignKey(to='teams.Team'),
        ),
        migrations.AddField(
            model_name='request',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
