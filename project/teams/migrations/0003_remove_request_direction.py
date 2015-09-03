# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='direction',
        ),
    ]
