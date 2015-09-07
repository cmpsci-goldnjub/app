# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_auto_20150907_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='description',
            field=models.TextField(help_text=b"Tell us about your project! Or don't. It's up to you!", blank=True, validators=[django.core.validators.MaxLengthValidator(2000)]),
        ),
    ]
