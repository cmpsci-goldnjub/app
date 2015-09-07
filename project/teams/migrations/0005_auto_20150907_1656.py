# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0004_auto_20150907_1655'),
    ]

    operations = [
        # Assign the default request foreign key to some garbage ID
        migrations.AddField(
            model_name='request',
            name='team',
            field=models.ForeignKey(default="527b257a-7153-4b99-94e8-40eca8581ad0", to='teams.Team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
