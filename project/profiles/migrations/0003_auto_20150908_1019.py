# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150907_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(default=b'stu', max_length=3, choices=[(b'css', b'Missouri S&T Computer Science Student'), (b'stu', b'Missouri S&T Student'), (b'fac', b'Missouri S&T Staff or Faculty'), (b'alm', b'Missouri S&T Alumnus/Alumna')]),
        ),
    ]
