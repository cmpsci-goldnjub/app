# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20150907_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
