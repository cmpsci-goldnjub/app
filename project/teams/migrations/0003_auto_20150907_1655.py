# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_team_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='team',
        ),
        migrations.RemoveField(
            model_name='team',
            name='members',
        ),
    ]
