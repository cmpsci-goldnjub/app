# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(default='stu', max_length=2, choices=[(b'css', b'Missouri S&T Computer Science Student'), (b'stu', b'Missouri S&T Student'), (b'fac', b'Missouri S&T Staff or Faculty'), (b'alm', b'Missour S&T Alumnus/Alumna')]),
            preserve_default=False,
        ),
    ]
